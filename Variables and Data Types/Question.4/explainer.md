Certainly! Here's the explanation with added code snippets:

```python
# Given a list of numbers [12, 34, 56, 78, 90], 
# create a new list that contains only the even numbers. 
# Print the original list and the new list.

# Define the list of numbers


# Use list comprehension to create a new list of even numbers
even_numbers = [num for num in numbers if num % 2 == 0]

# Print the original list and the new list of even numbers
print("Original list:", numbers)
print("Even numbers:", even_numbers)
```

Explanation:
 ```python
    numbers = [12, 21, 34, 43, 49, 56, 64, 78, 88, 90, 99]
    ```
-  Defines a list named `numbers` containing various integers.

```python
    even_numbers = [num for num in numbers if num % 2 == 0]
    ```

-  Utilizes list comprehension to create a new list named 
`even_numbers`. This new list contains only the even numbers from the original `numbers` list.


- `num % 2 == 0`: Checks if the element `num` is divisible by 2 (i.e., it's an even number).
- `print("Original list:", numbers)`: Prints the original list (`numbers`).
- `print("Even numbers:", even_numbers)`: Prints the list containing only the even numbers (`even_numbers`).