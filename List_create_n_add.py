def main():

    #creating a string list
    first_list = ["Milton", "Juan", "Rafaela", "Fernando"]
#positions > ........1º......2º........3º........4º.....
#index >...0.......1........2..........3.....

#......This line prints "Rafaela"...second index.
    print(first_list[2])

#adding a new item using .append

    first_list.append("new student")

    print(first_list)

# it is important to remember that the new student will be added at position 5 of the list and 4 in index.


     #creating a empty list

    empty_list = []

    print(empty_list)

    #adding a new int itens
    empty_list.append(4)
    empty_list.append(8)
    empty_list.append(12)

    print(empty_list)

    #creating a list using the built in method

    empty_list_builtin = list()
    print(empty_list_builtin)

    #creating a full list using built in

    full_list_builtin = list(["aqui", "tem", "coisa"])
    print(full_list_builtin)

    #Built in functions are external functions !!!



main()