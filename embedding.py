import torch
from torchvision.transforms import v2
from PIL import Image
import torchvision.models as models
from data import SaveData

class Vectorial:
    
    def __init__(self):
        self.modelos()
    
    def imgTrasnform(self, img):
        self.datataSet = SaveData()
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
        self.datataSet.save(self.imgVector)
        
        
    def similitud(self,cos_sim,therhold=0.90):
        return cos_sim >= therhold
    
    def comparacionCose(self):
        cos = torch.nn.functional.cosine_similarity
        outpus = cos()
            