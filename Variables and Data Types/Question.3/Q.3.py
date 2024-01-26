''' You have the following list of numbers: [1, 2, 3, 4, 5]. 
Convert each number to its corresponding string representation 
and store the results in a new list called str_numbers. Finally, 
print the str_numbers list. '''


# Solution

numbers = [1, 2, 3, 4, 5]
str_numbers = [str(num) for nun in numbers]
print(str_numbers)