numero = input("Escolha um numero para que o proximo jogador advinhe: ")
print("Nice job !", end="\r") #não funciona
chute = input("Tente advinhar o numero que o jogador um escolheu: ")

while chute != numero:

    if chute > numero:
        chute = input("Tente um numero menor: ")
    else:
        chute = input("Tente um numero maior: ")
else:
    print("Acertou !")