

1. **First Solution:**
   ```python
   name = "John"
   age = 30

   print("Hello", name, "! You are", age, "years old.")
   ```

   In this solution, predefined values for `name` and `age` are used. The `print` statement combines these values using commas. The output will be: "Hello John! You are 30 years old."

   You can also use an F-string for a more concise and readable format:

   ```python
   print(f"Hello {name}! You are {age} years old.")
   ```

2. **Second Solution:**
   ```python
   name = input("Your name: ")
   age = input("Your age: ")

   print(f"Hello {name}! You are {age} years old.")
   ```

   This solution allows the user to input their own values for `name` and `age` using the `input` function. The entered values are then used in the F-string to print a personalized greeting. The output will be based on the user's input.

In summary, the code demonstrates how to use variables, input functions, and string formatting to create a customized greeting message. The second solution is interactive, allowing users to input their own information.