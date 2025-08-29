#pyton program to check the validity of password

password = input("Enter a password: ")

if len(password) < 6:
    print("Password must be at least 6 characters long.")
elif len(password) > 16:
    print("Password must be at most 16 characters long.")
#make sure password have one letter between [a-z] and [A-Z]
elif not any(char.isalpha() for char in password):
    print("Password must contain at least one letter between [a-z] and [A-Z].")
#make sure password have one number between [0-9]
elif not any(char.isdigit() for char in password):
    print("Password must contain at least one number between [0-9].")
#make sure passworde have one special character[$#@]
elif not any(char in ['@', '#', '$'] for char in password):
    print("Password must contain at least one special character [$, #, @].")
else:
    print("Password is valid.")