import sys

#win_game = input (str("Digite o jogo vencedor: "))
win_game = ["03 22 10 12 43 38"] #esta pegando o /n
#cont = 0
int_games = []
#int_number = []

archive = open(sys.argv[1], "r", encoding='utf-8')
game_list = archive.readlines()

for games in game_list:
    
    if games == win_game:
        print("Jogo ganho")
    else:
        print("Jogo perdido.")
   




#to do:
    #change the list to matix;
    #compare with the win game;
    #count/separe the "quinas, senas e quadras";
    #print the "quinas, senas e quadras".




# "C:\Users\Milton\Documents\mega.txt"