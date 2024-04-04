# extract cherry from the nested list
list1 = [1,2,3,4, ['apple', 'banana', 'cherry']]

# nestedList = list1[4][1]   # First index gives the position of the nest list
# # print(nestedList)        # Second index gives the element from the nested list
#
# print(nestedList)


# change banana to kiwi inside the nested list

list1[4][1] = 'Kiwi'
print(list1)