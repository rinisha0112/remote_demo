

def get_countries():

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
            #langData[language].extend([string for string in list2 if string.isalpha()]
           langData[language].extend([list2[0]])
        else:
            #list3=[string for string in list2 if string.isalpha()]
            langData[language]=[list2[0]]

    print "\n\nFirst format: \n",langData

    print "\n\nSecond format: \n",
    
    for k in langData.keys():

        print k, " ", langData[k]


if __name__=='__main__':
    get_countries()
