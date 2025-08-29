
with open ('test.txt','w') as txt:
    txt.write("Hello World\n")
    txt.write("You are now at the end of Sir Marco Class\n")

data=''

with open('test.txt','r') as txt:
    data=txt.read()

words=data.split()
print(words)
