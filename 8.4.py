odd_sum = 0
even_sum = 0
for i in range(1,101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("The sum of odd numbers from 1 to 100 is", odd_sum)
print("The sum of even numbers from 1 to 100 is", even_sum)


