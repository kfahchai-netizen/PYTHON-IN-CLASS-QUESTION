print("\nScrabble Game")
score = {"a": 1, "b": 3, "c": 3, "d": 1, "e": 2,
"f": 2,"g": 4, "h": 1, "i": 4, "j": 5, "k": 8, "l": 3,"m": 1,
"n": 1, "o": 1, "p": 10, "q": 3, "r": 1,
"s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 4,
"y": 8, "z": 10}

word = input("Enter a word: ")
word = word.lower()

total = 0
print("\n*******************************")
print("* Letter\t* Score *")
print("*******************************")
for a in word:
    if a in word:
        print("*",a, "\t\t*",score[a]," *")
        print("*******************************")
    total += score[a]
print("Total:\t", total)