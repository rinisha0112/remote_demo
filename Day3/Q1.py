fh=open("empData.txt",'r')
empData={}
#fh=open("empData.txt",'r')
sum1=0
for line in fh:
    line=line.rstrip()
    list1=line.split(":")
    empData[list1[0]]=list1[1:]
    sum1=sum1+int(empData[list1[0]][-1])
print(empData)

k=empData.keys()
k.sort()

for i in k:
    print i, " ", empData[i]

print "Sum of salaries = ",sum1

    
