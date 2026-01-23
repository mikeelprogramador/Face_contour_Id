import faiss
import os

class SaveData:
    
    def __init__(self):
        self.rut = "data/DataSet.index"
        self.create()
        
    def create(self):
        if os.path.exists(self.rut):
            self.index = faiss.read_index("data/DataSet.index")
        else:
            dim = 512
            self.index = faiss.IndexFlatIP(dim)
            
    def save(self,vector):
        self.index.add(vector)
        faiss.write_index(self.index,"data/DataSet.index")
        
    
    def Similarites(self,input,therhold = 0.85):
        sim = 1
        similari, indice = self.index.search(input,sim)
        
        if indice[0][0] <=-1:
            print("No exite ningun dato")
        else:
            #return similari >= therhold
            print(similari)
            print(indice)
            print(similari[0][0] >= therhold)           


        