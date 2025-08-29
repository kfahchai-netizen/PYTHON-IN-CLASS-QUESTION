# the fibonacci series is the series of numbers in which each number is the sum of the two preceding numbers

print("Fibonacci Series")
first = int(input("Enter the starting value for Fibonacci series: "))
last = int(input("Enter the ending value for Fibonacci series: "))
a,b = 0,1
while a < last:
    if a >= first:
        print(a, end=' ')
    a, b = b, a + b
print()


