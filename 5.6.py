print ("B&B Inn")
print("""
Breakfast Menu
[A]merican Breakfast
[C]hinese Porridge
[N]asi Lemak
[F]ried Noodle
[L]aksa
[M]ee Mamak

""")

choice = input("What would you like to order? (A/C/N/F/L/M) ").upper()
potion=input("How many potion? ").upper()

if choice == "A":
    total = 12.5 * int(potion)

elif choice == "C":
    total = 6.30 * int(potion)

elif choice == "N":
    total = 5.50 * int(potion)

elif choice == "F":
    total = 5.50 * int(potion)

elif choice == "L":
    total = 5.30 * int(potion)

elif choice == "M":
    total = 4.8 * int(potion)


print("Total:",total)