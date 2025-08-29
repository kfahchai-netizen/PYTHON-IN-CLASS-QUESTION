name=str(input("Enter student names (separated by using commas): "))
marks = list(map(float, input("Enter student marks (separated by using commas): ").split(',')))
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Excellent Tuition Center")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

name_list = name.split(',')
mark_list = marks
for i in range(len(name_list)):
    mark = float(mark_list[i])
    if mark >= 80:
        grade = 'A'
    elif mark >= 70:
        grade = 'B'
    elif mark >= 60:
        grade = 'C'
    elif mark >= 50:
        grade = 'D'
    else:
        grade = 'F'
    print("Student Name:", name_list[i], "Mark:", mark, "Grade:", grade)


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Total marks:", sum(mark_list))
print("Average marks:", sum(mark_list)/len(mark_list))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")