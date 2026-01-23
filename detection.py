#Librerias necesarias
import cv2
from ultralytics import YOLO
import time
from embedding import Vectorial

"""
Documenatcion de la clase Program

Esta clase tiene la funcion en cargada del reconocimiento de dichos objetos atravez del model-face de yolo
otra funcion que tiene le permite administra la camara por defecto en el computador para que el modelo pueda hacer 
el reconocimiento de los objetos

"""

class Program:
    
    def __init__(self):
        self.model = YOLO("yolov8n-face.pt") #Se carga el modelo de deteccion de rostros
        self.embedding = Vectorial()
        self.key =  True 
        self.starTime = None
        self.run()
        
        
    def detectionFace(self, frame):
        """
        Documentacion de detectionFace
        
        :param self: Description
        :param frame: cadena visual que se recibe al momneto de ejecutar la camara
        
        Este metodo funciona gracias al model-face de yolo8
        El metod funciona principalmente para detectar unos objetos espeficicos
        
        :return fram: Estamos retornando la cadea visual modificada que se recibio como parametro
        """
        result = self.model(frame,verbose=False) #"verbose False" desactiva los comit que por defecto, envia ultralytics por consola
        r = result[0]
        
        label = None
            
        for box in r.boxes:
            x1,y1,x2,y2 = map(int, box.xyxy[0]) #Se extraen las cordenadas de la baja
            cls =  int(box.cls[0])
            conf = float(box.conf[0]) #Se extrae el umbral como un float
            
            if conf < 0.5:
                continue
            
            if conf > 0.8: 
                label = f"Buscando rostro. {conf:.2f}"#Si se quiere saber la umbral o la confianza
                color = (0,255,255)
                
            if conf >= 0.85:
                label = f"Rostro detectado. {conf:.2f}" 
                color = (0,255,0)
                
                if self.starTime is None:
                    self.starTime = time.time()
                elif time.time() - self.starTime >= 5:#Tiempo de espera para capturar el frame
                    saveFrame = frame[y1:y2, x1:x2] #Guarda el objeto 
                    #saveFrame = cv2.cvtColor(frame[y1:y2, x1:x2], cv2.COLOR_BGR2RGB) #Guarda el objeto 
                    self.embedding.imgTrasnform(saveFrame)
                    #cv2.imwrite("rostro.jpg",saveFrame)
                    print("frame guardado")
                    self.key = False
                    
        
        if label:
            cv2.rectangle(frame, (x1,y1), (x2,y2), color, 2)      #Forma de la caja, con su respectivo color       
            cv2.putText(frame, label, (x1, y1-5),                    #ubicacion del texto
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)                #tipo de letra con su tamaño y color
                
        return frame
                
    
    def run(self):
        """
        Documentacion de run
        
        :param self: Description
        
        Este metodo ejecuta la camara, para dar inicio al reconocimiento de objetos.
        """
        #Cargamos la camara por defecto
        cap = cv2.VideoCapture(0)
        
        while(cap.isOpened()):
            ret,frame = cap.read()
            
            if not ret:
                break
            elif ret == True:
                if self.key:
                    exitFrame = self.detectionFace(frame)
                else:
                    exitFrame = frame
                cv2.imshow('Camare',exitFrame)
                
                if cv2.waitKey(1) == 27: #Oprimir la letra ESC para cerrar la ventana
                    break
                
        cap.release()
        cv2.destroyAllWindows()
    

    def opctions(self, opc):
        
        """
        Documetacion de opctions
        
        :param self: Description
        :param opc: Description
        
        Este metodo esta planeado para ser un filtro en el cual, se puedan guardar los dato 
        y tambian usar otros metodos ajenos a la clase para comparalos.
        """
        
        if opc == -1: #cuando la opcion es -1 es el registro
            pass
        if opc == 1: #Cuando la opcion sea 1 es incio de sesion
            pass
            
            
# if __name__ == "__main__":
#     Program()

