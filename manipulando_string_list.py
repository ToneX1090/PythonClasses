# Character is a letter.
char="c"

#string is a character 'set'.

string_word="Tonex"
string_frase="Tonex é uma boa pessoa =)"

#print to you see in the screen:

print (char)
print (string_word)
print (string_frase)

# (Vector)Array is a sequency of elements with same type.

# String is a array of characteres !

string = "Maravilha"
#-index---012345678--

# printing the letter by index (var string)
print (string[0])
print (string[1])
print (string[2])
print (string[3])
print (string[4])
print (string[5])
print (string[6])
print (string[7])
print (string[8])

# IS NOT POSSIBLE REWRITE A STRING !!!

#string = "Maravilha"
#string[2] = "g"

#print (string) ## Error

# YOU CAN SLICE A STRING !

new_string = string[:2] + 'g' + string[3:]
#take all before index 2 + "g" + all after index 3
#---------Maravilha
#-index---012345678--
print (new_string)

# printing a string backwards letter by letter

print (new_string[-1])
print (new_string[-2])
print (new_string[-3])
print (new_string[-4])
print (new_string[-5])
print (new_string[-6])
print (new_string[-7])
print (new_string[-8])
print (new_string[-9])

# Search in a string (true or false)

#true
test ="b" in "abc"
print(test)

#false
test = "d" in "abc"
print(test)

#another way false
test = "b" not in "abc"
print(test)

#concatenate and switch between lower and upper

word = "Mil" + "Ton"
print (word)

#lower
word = "Mil".lower() + "Ton".lower()
print(word)

#upper
word = "Mil".upper() + "Ton".upper()
print(word)

# Return a string size
print(len(word))
#6 characteres

#checking if all characters are letters (.isalpha()) true/false

print("abc".isalpha())
print("a2c".isalpha())
print("124".isalpha())
print("++:/".isalpha())

#remove blank spaces .strip ust at the beginning and at the end

print("   enxugando espaços extra    ".strip())

#.join Join items using a delimiter

string = "abcdef"

print(",".join(string))
#Inserts a "," between elements (you can insert anything berween the " ", incluiding spaces)

#.split Separeta items using a delimiter

#separates in the spaces
string = "T o n e x"
print(string.split())

#separates in the ","
string = "T,o,n,e,x"
print(string.split(","))


