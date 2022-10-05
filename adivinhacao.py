import random

def jogar():
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("Bem vindo ao jogo de adivinhação!")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

    numero_sorteado = random.randrange(1, 101)
    tentativa = 0
    rodada = 1
    pontos = 1000

    print("Qual o nível do desafio?")
    print(" ")
    print("1 = Fácil; \n2 = Médio; \n3 = Difícil.")
    print(" ")
    nivel = int(input("Nível: "))

    if nivel == 1:
        tentativa = 10
    elif nivel == 2:
        tentativa = 5
    elif nivel == 3:
        tentativa = 3
    else:
        print("PAMBAM!! Escolha um nível de 1 a 3.")

    for rodada in range (1, tentativa + 1):
        print("Tentativa {} de {}".format(rodada, tentativa))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deveria digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_sorteado
        maior = chute > numero_sorteado
        menor = chute < numero_sorteado

        if(acertou):
            print("Você acertou o chute \nVocê fez {} pontos!!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O número que você chutou é maior que o escolhido.")
            elif(menor):
                print("Você errou! O número que você chutou é menor que o escolhido.")
            pontos_perdidos = abs(numero_sorteado - chute)
            pontos = pontos - pontos_perdidos


        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

    print("O número sorteado foi {}".format(numero_sorteado))

    print("Fim de Jogo!")


if(__name__ == "__main__"):
    jogar()