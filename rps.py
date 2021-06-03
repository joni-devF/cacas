import random


comp=random.randint(1,3)

if comp == 1:
    comp = "R"
elif comp == 2:
    comp = "P"
elif comp == 3:
    comp = "S" 

def game(comp):
        contP1 = 0
        contP2 = 0

        while contP1<2 and contP2<2:
    
            player2 = input("Ingrese R, P o S: ") 

            if comp == player2:
                print("Empate")
                print(f"el computador saco: {comp}")
                print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")

            if comp == "R" and player2 == "S":
                print("el computador gana")
                print(f"el computador saco: {comp}")
                contP1 = contP1 + 1
                print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
            elif player2 == "R" and comp == "S":
                print("el usuario gana")
                print(f"el computador saco: {comp}")
                contP2 = contP2 + 1
                print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")

            if comp == "P" and player2 == "R":
                print("el computador gana")
                print(f"el computador saco: {comp}")
                contP1 = contP1 + 1
                print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
            elif player2 == "P" and comp == "R":
                print("el usuario gana")
                print(f"el computador saco: {comp}")
                contP2 = contP2 + 1
                print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")

            if comp == "S" and player2 == "P":
                print("el computador gana")
                print(f"el computador saco: {comp}")
                contP1 = contP1 + 1
                print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
            elif player2 == "S" and comp == "P":
                print("el usuario gana")
                print(f"el computador saco: {comp}")
                contP2 = contP2 + 1
                print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")

        print("el computador ha ganado ", contP1 )
        print("el usuario ha ganado ", contP2)
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")

        if contP1 == 2:
            print("El computador ganó 2 veces")

        if contP2 == 2:
            print("El usuario ganó 2 veces")

salida=game(comp)