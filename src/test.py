# This file demonstrates an alternative version

# Arithmetic operation
m = 3
n = 14
floor_div = n // m  # Now uses floor division
print(f'Floor division of n by m: {floor_div}')

# List operations
mod_list = [0, 10, 20, 30]
mod_list.remove(10)  # Changed to remove 10
print(f'List with one item removed: {mod_list}')

# Conditional
if m * 2 > n:
    print('Twice m is greater than n')
else:
    print('Twice m is not greater than n')  # New logic and output

# Loop
for letter in ['p', 'q', 'r']:
    print(f'Reading letter: {letter}')

# Function
def echo(name):
    print(f'Echo: {name * 2}')  # Function now repeats name

echo('Designer')
