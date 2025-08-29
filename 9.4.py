def addition(n1, n2):
    ans = n1 + n2
    return ans

def subtraction(n1, n2):
    if n1 < n2:
        n1, n2 = n2, n1
    ans = n1 - n2
    return ans

def multiplication(n1, n2):
    ans = n1 * n2
    return ans

def division(n1, n2):
    if n1 < n2:
        n1, n2 = n2, n1
    ans = n1 / n2
    return ans

def inputnumber():
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
    return n1, n2

selection = ""
while selection != "Q":
    print("\nMathematical Calculator")
    print("""
    [A]ddition
    [S]ubtraction
    [M]ultiplication
    [D]ivision
    [Q]uit
    """)
    selection = input("Selection: ").upper()
    if selection == "Q":
        print("Thank you! Have a nice day!")
        break
    elif selection == "A":
        n1, n2 = inputnumber()
        print("Addition answer:", addition(n1, n2))
        print("-----------------------------------------------------")
    elif selection == "S":
        n1, n2 = inputnumber()
        print("Subtraction answer:", subtraction(n1, n2))
        print("-----------------------------------------------------")
    elif selection == "M":
        n1, n2 = inputnumber()
        print("Multiplication answer:", "{:.2f}".format(multiplication(n1, n2)))
        print("-----------------------------------------------------")
    elif selection == "D":
        n1, n2 = inputnumber()
        print("Division answer:", "{:.2f}".format(division(n1, n2)))
        print("-----------------------------------------------------")
    else:
        print("Invalid input. Please try again.")
        print("-----------------------------------------------------")
        
input("\nPress enter to terminate the program")

