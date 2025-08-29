items=[ ]
result_str="";
for row in range(0,10+1):
    for col in range(0,16+1):
        if(row==3 or row==7):
            result_str=result_str+"*"
        else:
           if(col==5 or col==11):
                result_str=result_str+"*"
           else:
                result_str=result_str+" "
    result_str=result_str+"\n"
print(result_str)