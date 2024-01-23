import sys

#win_game = input (str("Digite o jogo vencedor: "))
win_game = ["03 22 10 12 43 38"] #esta pegando o /n
#cont = 0
int_games = []
int_number = []
lista = [[1, 2, 3, 5, 4], [1, 5, 8, 6, 2], [8, 6, 9, 5, 2]]

archive = open(sys.argv[1], "r", encoding='utf-8')
game_list = archive.readlines()

for games in game_list:
    
    for game in games.split():
        int_number.append(int(game))
    int_games.append(int_number)

print(lista)
print(type(lista))
print(int_games)






#to do:
    #change the list to matix;
    #compare with the win game;
    #count/separe the "quinas, senas e quadras";
    #print the "quinas, senas e quadras".




# "C:\Users\Milton\Documents\mega.txt"