#calculate a dog age in human year

age= int(input("Enter your age in dog years: "))

if age<0:
    print("Invalid input. Please enter a positive number.")
elif age<1:
    new_age=age*15
elif age<=2:
    #the second year of a dog life is equal to 9 year of human life
    new_age=(15+9)
else:
    new_age=(15+9)+((age-2)*5)
print(f"The dog age in human years is {new_age}")