import sys

#win_game = input("Digite o jogo vencedor: ")
cont = 0

arquivo = open(sys.argv[1], "r", encoding='utf-8')
game_list_txt = arquivo.readlines()

for i in game_list_txt:
       print(i)

print (type(i))

#to do:
    #change the list to matix;
    #compate with the win game;
    #count/separe the "quinas, senas e quadras";
    #print the "quinas, senas e quadras".




# "C:\Users\Milton\Documents\mega.txt"