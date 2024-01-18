import sys

#win_game = input("Digite o jogo vencedor: ")
cont = 0
int_games = []
int_number = []

archive = open(sys.argv[1], "r", encoding='utf-8')
game_list_txt = archive.readlines()

for game in game_list_txt:

    for number in game:
        real_number = int(number.strip())
        int_number.append(real_number)
    int_games.append(int_number)

print(int_games)
print (type(int_games))
print(int_number)
print (type(int_number))

#to do:
    #change the list to matix;
    #compare with the win game;
    #count/separe the "quinas, senas e quadras";
    #print the "quinas, senas e quadras".




# "C:\Users\Milton\Documents\mega.txt"