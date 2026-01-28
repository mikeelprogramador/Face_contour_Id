import faiss
import os

class SaveData:
    
    def __init__(self):
        self.rut = "data/DataSet.index"
        self.__create()
        
    def __create(self):
        """
        Docstring for __create
        
        :param self: Description
        
        Este metodo hace valida si la base de datos existe, si no existe la crea
        """
        if os.path.exists(self.rut):
            self.index = faiss.read_index("data/DataSet.index")
        else:
            dim = 512
            self.index = faiss.IndexFlatIP(dim) #Se crea la datavectorial en coseno
            
    def __save(self,input):
        """
        Docstring for __save
        
        :param self: Description
        :param input: Entrada vectorial
        
        Este metodo agrega el vector a la base de datos vectorial
        """
        self.index.add(input)
        faiss.write_index(self.index,"data/DataSet.index")
        
    def searchPerson(self,input):
        """
        Docstring for searchPerson
        
        :param self: Description
        :param input: entrada vectorial
        
        Este metodo funciona principalmente para verificar si la persona ya esta registrada
        en caso cotario la agrega a la base de datos
        """
        similari,indice = self.index.search(input,1)
        if indice[0][0] >= 0:
            print("El sistema encontro datos existentes")
        else:
            self.__save(input)
            print("Datos guardados exitosamnete")
            
    def Similarites(self,input,therhold = 0.80):
        """
        Docstring for Similarites
        
        :param self: Description
        :param input: entrada vectorial
        :param therhold: umbral, ya esta predefinido
        
        El metodo comparas las si el vector de extrada tiene alguna similitud con uno de la base de datos
        para seguidamente hacer una similitud por metodo del coseno
        """
        similari, indice = self.index.search(input,1)
        
        if indice[0][0] >= 0:
            print(similari) # muestra las similitudes con conseno
            print(indice) # muestra la posicion de la array en la cual se encontro la similitud
            print(similari[0][0] >= therhold) 
        else:
          print("No exite ningun dato")


        