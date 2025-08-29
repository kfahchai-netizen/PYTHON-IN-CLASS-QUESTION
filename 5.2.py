months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print("List of months: " + ", ".join(months))

month_name = input("Input the name of Month: ")
if month_name.title() == "February":
    print("No. of days: 28/29 days")
elif month_name.title() in ("April", "June", "September", "November"):
    print("No. of days: 30 days")
elif month_name.title() in ("January", "March", "May", "July", "August", "October", "December"):
    print("No. of days: 31 days")
else:
    print("Invalid input")
