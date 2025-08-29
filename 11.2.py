txt=open('test.txt','w')

txt.write("Hello World\n")
txt.write("You are now at the end of Sir Marco Class\n")

txt.close

txt=open('test.txt','r')
str_read=txt.readlines()
print(str_read)

txt.close