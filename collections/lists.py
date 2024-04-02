myList = [1,2,3,4]
print(myList, "This is the original list")
myList.pop()       # this popups the last index value
print(myList, "last index value is removed")
myList.pop(0)      # this removes the value at the 0 index position
print(myList, "0th index value is removed")
myList[0] = 10     # this updated the value at the 0 index position
print(myList, "0th index value is updated with value 10")
myList[1] = ['hello', 'Pk']
print(myList, "1st index value is updated with new list")
print("the data type of myList is ", type(myList))




#
"""
[1, 2, 3, 4] This is the original list
[1, 2, 3] last index value is removed
[2, 3] 0th index value is removed
[10, 3] 0th index value is updated with value 10
[10, ['hello', 'Pk']] 1st index value is updated with new list
the data type of myList is  <class 'list'>
"""