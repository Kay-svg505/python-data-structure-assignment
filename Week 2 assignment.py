#create an empty list
my_list =[]
print(my_list)

#append elements to my list
my_list.append (10)
my_list.append (20)
my_list.append (30)
my_list.append (40)
print(my_list)

#insert 15 at the second position (index 1)
my_list.insert(1,15)
print(my_list)
 
#extend list 
my_list.extend([50,60,70])
print(my_list)

#remove last element
my_list.pop()
print(my_list)

#sort list in ascending order
my_list.sort()


#find index of the value of 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)

#print final list
print("Final List:",my_list)
