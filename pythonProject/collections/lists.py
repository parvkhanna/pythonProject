myList = [1,2,3,4]
print(myList, "This is the original list")


newMyList = myList.pop()       # this popups the last index value|| Pop method returns the value of the index value which is removed
print(newMyList, "last index value is removed")
print(myList, " is the new list")


myList.pop(0)      # this removes the value at the 0 index position
print(myList, "0th index value is removed")


myList[0] = 10     # this updated the value at the 0 index position
print(myList, "0th index value is updated with value 10")


myList.append(1993)
print(myList, "number is appended to myList")


myList[0] = ['hello', 'Pk']
print(myList, "1st index value is updated with new list")

#Similaryly we can use append method to add the list object to the original list object

myList.append([10,3,1993])
print(myList, "This appends the new list object to the original list")

myList.pop()
print(myList, "last list value is")


size = len(myList)
print("size of the list is" , size)



list1 = [1,2,3,4,5,6,7,8]
list2 = [9,10,11,12,13,14]

list1.append(list2)
print(list1, "This adds the list2 as an element to the last index position")

#
list3 = [1,2,3,4,5,6,7,8]
list4 = [9,10,11,12,13,14]
list = list3 + list4
print(list, "This merges list 1 and list 2 ")


# Output
"""
[1, 2, 3, 4] This is the original list
4 last index value is removed
[1, 2, 3]  is the new list
[2, 3] 0th index value is removed
[10, 3] 0th index value is updated with value 10
[10, 3, 1993] number is appended to myList
[['hello', 'Pk'], 3, 1993] 1st index value is updated with new list
[['hello', 'Pk'], 3, 1993, [10, 3, 1993]] This appends the new list object to the original list
[['hello', 'Pk'], 3, 1993] last list value is
size of the list is 3
[1, 2, 3, 4, 5, 6, 7, 8, [9, 10, 11, 12, 13, 14]] This adds the list2 as an element to the last index position
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] This merges list 1 and list 2 
"""