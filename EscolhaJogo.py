import forca
import adivinhacao

def escolha_jogo():
    print("-=-=-=-=--=-=-=--=-")
    print("Escolha o seu jogo!")
    print("-=-=-=-=-=-=-=-=-=-")
    
 
    print("(1) Forca \n(2) Adivinhação")

    escolha = int(input("Qual é o jogo? "))

    if(escolha == 1):
        print("Jogando Forca")
        forca.jogar()

    elif(escolha == 2):
        print("Jogando Adivinha")
        adivinhacao.jogar()


if(__name__ == "__main__"):
    escolha_jogo()