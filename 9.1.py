print("~User Input~")
a=float(input("First number: "))
b=float(input("Second number: "))
c=float(input("Third number: "))

def max_of_three(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

def min_of_three(a,b,c):
    if(a<b and a<c):
        return a
    elif(b<a and b<c):
        return b
    else:
        return c

print("\n~Output~")
print("Largest:",max_of_three(a,b,c))
print("Smallest:",min_of_three(a,b,c))

