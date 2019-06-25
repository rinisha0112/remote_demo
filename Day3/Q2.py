f=open("country.txt",'r')
langData={}


for  list1 in f:

    #list1=f.readline()
    #print list1
    list1=list1.rstrip()
    list2=list1.split(',')
    #print list2
    language=list2[-1]
    if langData.has_key(language):
        langData[language]=langData[language]+1
    else:
        langData[language]=1

print langData

for k in langData.keys():

    print k, " ", langData[k]

