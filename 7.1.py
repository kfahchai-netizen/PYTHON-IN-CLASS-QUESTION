#create a multiplication table (from 1to 10) for interger entered by user

num = int(input("Enter a number: "))

for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")