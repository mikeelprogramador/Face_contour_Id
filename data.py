import faiss

class SaveData:
    
    def __init__(self):
        self.dim = 512
        self.index = faiss.IndexFlatL2(self.dim)
    
    def save(self,vector):
        self.index.add(vector)
        faiss.write_index(self.index,"data/DataSet.index")
        
    def loadingFiles(self):
        return faiss.read_index("data/DataSet.index")