#write a pyton program to find number between 100 to 400, where each digit of the number is even number. The number obtained should print in a comma-separated sequence


for i in range(100, 401):
    digits = [int(x) for x in str(i)]  
    if digits[0] % 2 == 0 and digits[1] % 2 == 0 and digits[2] % 2 == 0:
        print(i, end=', ')
