'''Write a Python program that declares two variables, name and age. 
Assign your name to the name variable and your age to the age variable. 
Then, print a message that says "Hello, [name]! You are [age] years old." '''

# First Solution
name = "John"
age = 30

print("Hello", name, "!You are", age, "years old.")

# You can use the Fstring
print(f"Hello {name}! you are {age} years old.")



# Second Solution
name = input("Your name: ")
age = input("Your age: ")

print(f"Hello {name}! you are {age} years old.")



