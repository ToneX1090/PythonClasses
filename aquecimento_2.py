import sys

win_game = input (str("Digite o jogo vencedor: "))

archive = open(sys.argv[1], "r", encoding='utf-8')
game_list = archive.readlines()
win_numbers = set(win_game.split(" "))


for game in game_list:

    numbers = game.strip().split(" ")
    correct_numbers = 0
    for number in numbers:
        if number in win_numbers:
            correct_numbers += 1
    if correct_numbers == 4:
        print(game + "\nÉ uma quadra.\n")
    elif correct_numbers == 5:
        print(game + "\nÉ uma quina!\n")
    elif correct_numbers == 6:
        print("\nLarga tudo que você está rico!\n")
    else:
        print(game + "\n" + str(correct_numbers) + " corretos\n")
            

# "C:\Users\Milton\Documents\mega.txt"