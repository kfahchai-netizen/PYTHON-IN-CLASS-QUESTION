#print the factorial entered by the user until the user click x/X

num=int(input("Enter a number: "))

while True:
    num = input("Enter a number (or 'X' to exit): ")
    if num.lower() == 'x':
        print("Thank you for using this program")
        break

    num = int(num)
    factorial = 1
    if num == 0:
        print("Factorial of 0 is 1")
        continue
    for i in range(1, num + 1):
        factorial = factorial * i

    print("Factorial of", num, "is", factorial)
