def main():

    list = [1,2,3,4,5,6,7,8,9,85]

    #structure variable = list[from index : to index]

    first_list = list[2:5] # take the values between 2 and 5
    second_lis = list[:7]  # take all the values until the index 7
    third_list = list[3:]  #take all values starting in the index 3 to the final of the list.

    print(first_list)
    print(second_lis)
    print(third_list)

    #IMPORTANT !!!! > the first index includes itself, the last index excluides itself (it's not appear)
    # index          0,1,2,3,4,5,6,7,8,9
    # list          [1,2,3,4,5,6,7,8,9,85]
    # firs_list      x,x,2,3,4,5*,x,x,x,x
    # second_list    0,1,2,3,4,5,6,7*,x,x,x
    # third_list     x,x,x,3,4,5,6,7,8,9
main()