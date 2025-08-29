initial_value=int(input("Enter initial number: "))
ending_value=int(input("Enter ending value: "))
counter=int(input("Enter decrease counter value: "))

if(initial_value<ending_value):
    initial_value,ending_value=ending_value,initial_value

if(counter>0):
    str_counter=str(counter)
    str_counter="-"+str_counter
    counter=int(str_counter)

print("\nThe numbers are:")
for x in range(initial_value,ending_value,counter):
    print(x,end=" ")

total=count=0
print()
for y in range(initial_value,ending_value,counter):
    total+=y
    count+=1

print("Total:",total)
print("Average:",total/count)