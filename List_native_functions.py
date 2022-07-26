#first function => append() Insert a element in the final of the list

numbers = ["one"]
print(numbers)
numbers.append("two")
print(numbers)
numbers.append("three")
print(numbers)

print("\n")

#Second function Index() => Return a Index of one determined element
lenguages = ["Python", "Java", "C+", "VB"]
# Indexes ------0---------1-----2-----3---

print(lenguages.index("C+"))

# Is possible assing it to a variable

index_lenguages =lenguages.index("Python")
print(lenguages.index("Python"))

print("\n")

#Seventh fuction => Sort the numbers of the list

list = [2, 4, 1]
print(list)

list.sort()
print(list)
# Is not possible to assing it to a variable : list2 = list.sort()

print("\n")

#---------Sort with strings---------
list = ["a","d","b","c"]

print (list)
print(sorted(list))
# is posible assing it to a variable:
list2 = sorted(list)
print (list2)