'''Given a list of numbers [12, 34, 56, 78, 90], 
create a new list that contains only the even numbers. 
Print the original list and the new list. '''

numbers = [12, 21, 34, 43, 49, 56, 64, 78, 88, 90, 99,]
even_numbers = [num for num in numbers if num % 2 == 0]
print("Original list:", numbers)
print("Even numbers:", even_numbers)


x = "y"
y = "x"
print(x is y)