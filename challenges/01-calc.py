# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

# Create a simple calculator that first asks the user what method they would like
# to use (addition, subtraction, multiplication, division) and then asks the user
# for two numbers, returning the result of the method with the two numbers. Here
# is a sample prompt:

# What calculation would you like to do? (add, sub, mult, div)
# add
# What is number 1?
# 3
# What is number 2?
# 6
# Your result is 9

prompt= '>'
print('What calculation would you like to do? (add, sub, mult, div')
calc = input(prompt)

print('What is number 1?')
num1 = input(prompt)

print('What is number 2?')
num2 = input(prompt)

if calc == 'add':
    result = int(num1) + int(num2)
elif calc == 'sub':
    result = int(num1) - int(num2)
elif calc == 'mult':
    result = int(num1) * int(num2)
elif calc == 'div':
    result = int(num1) / int(num2)


print(f'Your result is {result}')