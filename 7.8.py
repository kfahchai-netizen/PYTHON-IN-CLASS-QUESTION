c_ans = 'c'

# This while loop will continue to execute as long as the user enters 'c' or 'C' when prompted.
# The loop will break if the user enters anything other than 'c' or 'C' (case insensitive).
while c_ans.lower() == 'c':
    print("~~ While Loop Program ~~\n")
    s_value = int(input("Enter initial value: "))
    e_value = int(input("Enter ending value: "))
    counter = int(input("Enter counter value (non-zero): "))

    if counter == 0:
        print("\nCounter cannot be zero. Please enter a valid counter value.")
        continue

    if counter < 0 and s_value < e_value:
        s_value, e_value = e_value, s_value
        print("The initial and ending values are swapped.")

    elif counter > 0 and s_value > e_value:
        s_value, e_value = e_value, s_value
        print("The initial and ending values are swapped.")

    print("\nLoop:")
    # This loop will start from the initial value, and
    # stop when it reaches the ending value. The loop
    # will increment by the counter value. If the
    # counter is positive, the loop will increment, if
    # it is negative, the loop will decrement. If the
    # counter is zero, the loop will not execute.
    for x in range(s_value, e_value + (1 if counter > 0 else -1), counter):
        print(x)
    # Ask the user for the new ending value
    e_value = int(input("Enter ending value: "))
    print("To increase/decrease the values in the loop")
    # Ask the user for the new counter value
    counter = int(input("Enter counter value: "))

    if counter == 0:
        print("\nCounter cannot be zero. Please enter a valid counter value.")
        continue  # Restart the loop to re-enter valid inputs

    if counter < 0:
        # Ensure values are swapped for decremental loop
        # so that the loop decrements from the initial value
        # to the ending value.
        if s_value < e_value:
            s_value, e_value = e_value, s_value
            print("The initial and ending values are swapped.")

        print("\nDecremented Loop:")
        # This loop will start from the initial value, and
        # stop when it reaches the ending value. The loop
        # will decrement by the counter value.
        x = s_value
        while x >= e_value:
            print(x)
            x += counter  # Decrement by counter

    else:
        # Ensure values are swapped for incremental loop
        if s_value > e_value:
            s_value, e_value = e_value, s_value
            print("The initial and ending values are swapped.")

        print("\nIncremental Loop:")
        x = s_value
        while x <= e_value:
            print(x)
            x += counter  # Increment by counter

    c_ans = input("\nEnter 'c' to continue or any other key to exit: ")

print("\n~~ Thank you for using the program ~~")



