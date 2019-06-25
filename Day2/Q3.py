empData={'1a':2500, '2a':3500}

print "Hello user, press 1 when done adding employee details."
flag=0
while(flag==0):
    str1=raw_input("Enter key:value pair")
    if ":" in str1:
        
        list1=str1.split(":")
        empData[list1[0]]=int(list1[1])
    elif(str1=="1"):
        flag=1;

    else:
        print "Incorrect format! please re-enter data in emp_id:salary format"

print "INSERTED EMPLOYEE DETAILS: \n", empData

k=empData.keys()
k.sort()
sorted_empData={i:empData[i] for i in k }
print "SORTED EMPLOYEE DETAILS: \n",sorted_empData


updated_empData={i:empData[i]+5000 for i in k}


print "UPDATED EMPLOYEE DETAILS: \n",updated_empData

        
    
