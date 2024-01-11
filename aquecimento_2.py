import sys

#win_game = input("Digite o jogo vencedor: ")
cont = 0

arquivo = open(sys.argv[1], "r", encoding='utf-8')
game_list_txt = arquivo.readlines()

for i in game_list_txt:
       print(i)

print (type(i))






# "C:\Users\Milton\Documents\mega.txt"