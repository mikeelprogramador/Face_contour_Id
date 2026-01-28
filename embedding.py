import torch
from torchvision.transforms import v2
from PIL import Image
from facenet_pytorch import MTCNN, InceptionResnetV1
#import torchvision.models as models
from dataVectorial import SaveData

# importante
# Impementar la verificacion al de la perosna al momento de registrarse, ya que puede general un error en la data vectorial 
# si una perosna llega a tener mas de un registro de su contorno facial



class Vectorial:
    """
    Docstring for Vectorial
    
    esta clase transforma la imagen a un input que el modelo pueda comprender, para seguidamente ese dato
    resultante convertirlo en un vector unidimencional
    """
    
    def __init__(self):
        self.__model()
        
    
    def imgTrasnform(self, img,forentkey):
        """
        Docstring for imgTrasnform
        
        :param self: Description
        :param img: dato del frame/array ingresado 
        :param forentkey: llave que permite opciones de recorido al flujo
        
        trasnforma el dato ingreado en el parametro img y lo conviertre en un tensor de 3 dimenciones
        """
        self.datataSet = SaveData()
        self.forentkey = forentkey
        imgTras = Image.fromarray(img)
    
        trasnform = v2.Compose([
            v2.ToImage(),
            v2.Resize((224,224), antialias=False),
            v2.ToDtype(torch.float32, scale=True),
            v2.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            )   
        ])

        self.tensorImg = trasnform(imgTras)
        self.__resizingVector()
        

    def __model(self):
        """
        Documnetacion de model
        
        :param self: Description
        
        En metodo es donde se carga el modelo face embedding 
        el cual es un modelo de la libreria facenet-pytorch
        
        https://github.com/timesler/facenet-pytorch
        """
        self.mtcnn = MTCNN(image_size=225,margin=225)
        self.resnet = InceptionResnetV1(pretrained='vggface2').eval()
        
        
    def __resizingVector(self):
        """
        Docstring for resizingVector
        
        :param self: Description
        
        El metodo resizingVector se encarga de de ajustar el tensor
        para convertir dicho input en un vector unidimencional
        """
        
        with torch.no_grad():#desactivamos el calculo de los gradianes
            self.imgVector = self.resnet(self.tensorImg.unsqueeze(0))#agregamos una dimencion de tamaño 1 al incio princio
            
        #Convertimos el vector multidimencional a un vector unidimencional
        self.imgVector = self.imgVector.flatten(1)
        
        #Normalizamos el vector 
        self.imgVector = torch.nn.functional.normalize(self.imgVector, dim=1)
        
        # print(self.imgVector.shape)
        self.opctions()

        
    
    def opctions(self):
        
        """
        Documetacion de opctions
        
        :param self: Description
        :param opc: Description
        
        Este metodo esta planeado para ser un filtro en el cual, se puedan guardar los dato 
        y tambian usar otros metodos ajenos a la clase para comparalos.
        """
        
        if self.forentkey == -1: #cuando la opcion es -1 es el registro
            self.datataSet.searchPerson(self.imgVector)
            
        if self.forentkey == 1: #Cuando la opcion sea 1 es incio de sesion
            self.datataSet.Similarites(self.imgVector)