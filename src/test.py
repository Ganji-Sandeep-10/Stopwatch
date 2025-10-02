# Arithmetic
num1 = 10
num2 = 20
sum_result = num1 + num2
print(f"The sum of {num1} and {num2} is: {sum_result}")

# List operations
my_list = [1, 2, 3, 4, 5]

my_list.append(6)
print(f"List after appending: {my_list}")

my_list.remove(2)


print(f"Length of the list: {len(my_list)}")

# Conditional
if num1 == 10:  # use '==' for comparison
    print("num1 is 10")

# Loop
for i in range(5):
    print(i)

# Function
def my_function():
    print("Hello from function")

my_function()  # call the function

# Factorial function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial n - 1)

num = int(input("Enter a non-negative number: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {num} is: {factorial(num)}")
