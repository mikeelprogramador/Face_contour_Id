import detection

"""
Este proyetco es de Autoria de Santiago Sanchez

El proyecto esta diseñado en pyhton version 3.9

Recomedacion del programador:
A media de que el proyecto vaya avanzado se ira actualizando
por el momento para que funcione correctamnete tendras que instalar unas librerias.

Recomensable crean un entorno para instalar las librerias 
que se encuentras en el requirements.txt 


"""

print("""
      Beta 1.3
      Bienvido al sistema de reconocimiento
    """)

appi = detection.Program()
    
while True:
    opc = 0
    
    if opc == 0:
        print("""
                Elige una opcion
                1 - registrarse
                2 - iniciar sesio
                3 - salir
            """)
    
    try:
        opc = int(input())
        
        if opc == 1:
            try:
                appi.run(-1)
                print("Registro finalizado")
            except Exception as e:
                print(e)

        if opc == 2:
            try:
                appi.run(1)
            except Exception as e:
                print(e)
            
        if opc == 3:
            print("Gracias por haber visitado el programa, hsata pronto :)")
            break
        
    except:
        print("El dato ingrsado no coincide")
        
   