#!python3  
import random
import numpy
import json

#Función que valida si el psio ingresado es correcto
def ValidarPiso(Piso):
    Pisos=[]
    for i in range(1,30):
      Pisos.append(i); 

    for n in Pisos:      
        if Piso != n:
            Validation = False
        else:
            Validation = True
        if Validation:
            return True

#Función donde se reliaza principalmente toda la logica del problema
def Logica(PisosIngresado,ArPisos,PisoInicial):

  #Declaración de variables
  inicial=0
  regresoDesde=0
  Valor=""
  valorPiso={}
  direccion=["Subiendo..","Bajando..","Detenido"]
  
  #Impresiones de retro alimentación
  print("Bienvenido")
  print("Piso inicial de ejecución: "+str(PisoInicial))
  print("Proximos pisos "+ str(ArPisos))
  print("Digite el piso al que desea ir")

  #Obtención del valor digitado y despues añadido al arreglo de proximos pisos
  valor=input()
  valor=int(valor)
  ArPisos.append(valor)

  #Creación del objeto JSON donde e mostrata el mapa de pisos ingresados al final del proceso
  valorPiso={f"{PisoInicial}": f"{valor}"}
  PisosIngresado.append(valorPiso)
  
  print("El mapa de pisos ingresados hasta hora es :")
  print(PisosIngresado)
  
  #Condición que validad si el piso ingresado, existe
  if ValidarPiso(valor):
    #Ciclo que funciona cuando el elevador esta subiendo      
    for n in range(PisoInicial,29+1,1):
        
        #Proceso para conocer hasta que piso es necesario que llegue el ascensor, guardandolo en la variable "inicial" 
        Tamaño=numpy.size(ArPisos)
        inicial=ArPisos[0]
        for t in range(0,Tamaño,1):
          if ArPisos[t]>inicial:
            regresoDesde=ArPisos[t]
            inicial=ArPisos[t]         
        #Condición que termina el ciclo, cuando el elevador haya llegado al ultimo piso necesario que suba 
        if n==inicial:
          break

        #Condición que valida si alguno de los pisos seleccionados se escuentra en la dirección en la cual se dirige el elevador
        if n==ArPisos[0] or n==ArPisos[1] or n==ArPisos[2] or n==ArPisos[3] or n==ArPisos[4]:
          
          #Impresiones que retroalimentan el piso en que se encuentra y si esta detenido
          print("Proximos Pisos "+ str(ArPisos))
          print("El piso actual es: "+str(n))
          print(direccion[0])
          print(direccion[2])         

          #Se le da la opción al usuario de ingrear otro piso, si lo desea
          print("Desea ingresar un piso 1-Si 0-No")
          valor2=input()
          valor2=int(valor2)

          #Validación de la respuesta del usuario
          if valor2==1:
            
            #Se solicita el piso que desea ingresar
            print("Ingrese el piso al que desea ir")
            valor=input();
            valor=int(valor)
            
            #Se agrega el piso en que se encuentra y el piso que se ingresó, al mapa de pisos ingresados
            valorPiso={f"{n}": f"{valor}"}
            PisosIngresado.append(valorPiso)
            
            #Se remueve el piso en el cual el elevador ya se detuvo
            for t in ArPisos:
              if t == n:
                ArPisos.remove(t)

            #Se agrega el piso ingresado al arreglo de proximos pisos, si el valor ingresado esta entre 1 y 29, si no lo esta se agrega un 0
            if valor>=1 and valor<=29:
              ArPisos.append(valor) 
              print(ArPisos)
            else:
                print("Digite un numero del 1 - 29")
                ArPisos.append(0)

          else:
            #Se agrega el piso ingresado al JSON de mapa de pisos, si el valor ingresado esta entre 1 y 29, si no lo esta se agrega un 0
            for t in ArPisos:
              if t == n:
                ArPisos.remove(t)

            print("Como no agrego un piso, agregamos el piso 0 el cual no existe, para continuar")    

            valorPiso={f"{n}": f"{0}"}
            PisosIngresado.append(valorPiso)
            
            ArPisos.append(0)            
          
        #Se da una retroalimentación de los pisos por los cuales se esta pasando     
        print("Elevador en el piso: "+str(n))
        print(direccion[0])  

    #Al acabar el ciclo de subida, empieza el de bajada, mostrando a partir de que piso se empieza a bajar
    print("Elevador regresando desde el piso " + str(regresoDesde))
    for n in range(regresoDesde,0,-1):
              
              #Condición que valida si alguno de los pisos seleccionados se escuentra en la dirección en la cual se dirige el elevador
              if  n==ArPisos[0] or n==ArPisos[1] or n==ArPisos[2] or n==ArPisos[3] or n==ArPisos[4]:
                
                #Impresiones que retroalimentan el piso en que se encuentra y si esta detenido
                print("Proximos Pisos "+ str(ArPisos))
                print("El piso actual es: "+str(n))
                print(direccion[1])
                print(direccion[2])

                #Se le da la opción al usuario de ingrear otro piso, si lo desea     
                print("Desea ingresar un piso 1-Si 0-No")
                valor2=input()
                valor2=int(valor2)

                #Validación de la respuesta del usuario
                if valor2==1:
                  #Se solicita el piso que desea ingresar
                  print("Ingrese el piso al que desea ir")
                  valor=input();
                  valor=int(valor)
                  
                  #Se agrega el piso en que se encuentra y el piso que se ingresó, al mapa de pisos ingresados
                  valorPiso={f"{n}": f"{valor}"}
                  PisosIngresado.append(valorPiso)                 
                 
                  #Se remueve el piso en el cual el elevador ya se detuvo
                  for t in ArPisos:
                    if t == n:
                      ArPisos.remove(t)

                  #Se agrega el piso ingresado al arreglo de proximos pisos, si el valor ingresado esta entre 1 y 29, si no lo esta se agrega un 0  
                  if valor>=1 and valor<=29:
                    ArPisos.append(valor) 
                    print(ArPisos)
                  else:
                      print("Digite un numero del 1 - 29")
                      ArPisos.append(0)
                else:
                  #Se agrega el piso ingresado al JSON de mapa de pisos, si el valor ingresado esta entre 1 y 29, si no lo esta se agrega un 0
                  for t in ArPisos:
                    if t == n:
                      ArPisos.remove(t)

                  print("Como no agrego un piso, agregamos el piso 0 el cual no existe, para continuar")    
                  valorPiso={f"{n}": f"{0}"}
                  PisosIngresado.append(valorPiso)
                  
                  ArPisos.append(0)
              
              #Se da una retroalimentación de los pisos por los cuales se esta pasando 
              print("El piso actual es: "+ str(n))
              print(direccion[1])
    #Por último, se imprime el mapa de pisos ingresados
    print("El mapa de pisos ingresados es :")
    print(PisosIngresado)

  else:         
        print("Digite un numero del 1 - 29, empiece de nuevo")
             
def Inicio():

    #Se declaran las varibles y arreglos que deben ser enviados a la función
    pisos=[]
    pisos=[15,27,13,10]
    PisoInicial = random.randint(1, 29)#El piso inicial es definido por medio de un random del 1 al 29.
    PisosIngresado=[]
    
    #Llamado a la función logica, enviando los parametros
    Logica(PisosIngresado,pisos,PisoInicial)

    
            
Inicio() #Se llama a la primera función que inicia todo