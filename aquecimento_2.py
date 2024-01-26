import sys

#win_game = input (str("Digite o jogo vencedor: "))
win_game = "03 22 10 12 44 38" #esta pegando o /n
#cont = 0

archive = open(sys.argv[1], "r", encoding='utf-8')
game_list = archive.readlines()
win_numbers = set(win_game.split(" "))


for game in game_list:

    numbers = game.strip().split(" ")
    correct_numbers = 0
    for number in numbers:
        if number in win_numbers:
            correct_numbers += 1
    
   
    
    print(game + " - " + str(correct_numbers) + " corretos")
            
    """ if correct_numbers == 4:
        print(game + " - É uma quadra.")
    elif correct_numbers == 5:
        print(game + " - É uma quina!")
    elif correct_numbers == 6:
        print(" Larga tudo que você está rico!")"""






# "C:\Users\Milton\Documents\mega.txt"