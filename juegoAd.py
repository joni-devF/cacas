
import random

randomNum = random.randint(0,20) 


def findNumber(num):
    cont = 0           
    salida = 4         
    while cont<=3:
        tunumero=int(input("introduce un numero: "))
        if tunumero == num:
            print("felicidades, lo lograste pendejo")
            break
        else:
            print("introduce tu numero de nuevo")
            
            salida= salida -1
            cont+=1
            print(f"el numero de intentos es: {salida}")


salida = findNumber(randomNum)