noList=[]

for i in range(2000,3000+1):
    if(i%8==0)and(i%10==0):
        noList.append(i)

for x in range(0,len(noList)):
    print(noList[x],end=",")
