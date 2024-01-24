import sys

#win_game = input (str("Digite o jogo vencedor: "))
win_game = "03 22 10 12 43 38" #esta pegando o /n
#cont = 0
int_games = []
#int_number = []
#lista = [[1, 2, 3, 5, 4], [1, 5, 8, 6, 2], [8, 6, 9, 5, 2]]

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


   
    print()





#to do:
    #change the list to matix;
    #compare with the win game;
    #count/separe the "quinas, senas e quadras";
    #print the "quinas, senas e quadras".




# "C:\Users\Milton\Documents\mega.txt"