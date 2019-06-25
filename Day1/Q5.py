

unsortedList = ['Aaaa', 'bb', 'cccccccc', 'zzzzzzzzzzzz']

sortedList=sorted(unsortedList, key=len)
print(sortedList)

"""
length_list=[]

for i in range(len(unsortedList)):

    length_list.append(len(unsortedList[i]))

sortedList=[]

for i in range(len(unsortedList)):

    g=length_list.argmin()
    sortedList.append(unsortedList[g])
    
"""
