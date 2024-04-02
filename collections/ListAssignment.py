#print the 1st three elements from list 1 after sorting and in reverse order
#print the last three elements from list 2 after sorting and in reverse order

list1 = [3,6,1,5,2,4]
list2 = ['z','x','y','c','a','b']


list1.sort()
list1 = list1[:3]
print(list1)

list2.sort()
list2 = list2[3:]
print(list2)

list = list1 + list2
print(list)
