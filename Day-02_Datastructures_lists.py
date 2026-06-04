# Datastructure
# Lists
list1 = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
#print(list1)

list2 = ['apple', [8,7,6,5], 'banana', 'cherry']
#print(list2)
#print(list2[0])
#print(list2[1])
#print(list2[1][0])
#print(list2[1][1])
#print(list2[1][2])
#print(list2[1][3])

#print(list2[-1])

list1.append('grape')
#print(list1)

list1.extend(['watermelon', 'pineapple'])
#print(list1)

del list1[5]
#print(list1)

list1.remove('banana')
#print(list1)

print(list1.pop(1))
#print(list1)

list2.clear()
#print(list2)

list1.reverse()
print(list1)   
