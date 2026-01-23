import torch
from torchvision.transforms import v2
from PIL import Image
import torchvision.models as models
from data import SaveData

class Vectorial:
    
    def __init__(self):
        self.modelos()

    
    def imgTrasnform(self, img,forentkey):
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
        self.resizingVector()
        
    def modelos(self):
        self.model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
        self.model.eval()
        self.model = torch.nn.Sequential(*list(self.model.children())[:-1])
        
    def resizingVector(self):
        with torch.no_grad():
            self.imgVector = self.model(self.tensorImg.unsqueeze(0))
            
        #Se convierte el vector a uno unidemncional
        self.imgVector = self.imgVector.flatten(1)
        
        #Normalizamos el vector 
        self.imgVector = torch.nn.functional.normalize(self.imgVector, dim=1)
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
            self.datataSet.save(self.imgVector)
            
        if self.forentkey == 1: #Cuando la opcion sea 1 es incio de sesion
            self.datataSet.Similarites(self.imgVector)