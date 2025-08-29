#a phyton file that will dislay the odd number and even number from the number entered by user

number = int(input("Enter a number (separated by comma): "))

# List comprehension to create a list of odd numbers from 1 to the given number
odd_numbers = [num for num in range(1, number + 1) if num % 2 != 0]

# List comprehension to create a list of even numbers from 1 to the given number
even_numbers = [num for num in range(1, number + 1) if num % 2 == 0]

print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)
