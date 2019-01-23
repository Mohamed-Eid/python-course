#lists
mylist = [1,2,4]
mylist = ['test',12,43.4,True,[1,2,3]]

print(mylist)
print(len(mylist))

mylist.append("newItem")
print(mylist)
mylist.append(['x','y','z'])
print(mylist)

mylist.extend(['x','y','z'])
print(mylist)
#remove end of the list
mylist.pop()
print(mylist)
#remove item by index
index = 0
mylist.pop(index)
print(mylist)




#list comprehensions
matrix = [[1,2,3],[4,5,6],[7,8,9]]
col1 = [row[0] for row in matrix]
print(col1)
