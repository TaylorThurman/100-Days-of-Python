# Exercise 1
print('''Day 1 - Python Print Function
The function is declared like this:
print('what to print')''')

# Exercise 2
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

# Exercise 3
name = input("What is your name? ")
print(len(name))

# Exercise 4
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

temp = a
a = b
b = temp

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

# Exercise 5
print("Welcome to the Band Name Generator.")
city = input("What's name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + city + " " + pet)
