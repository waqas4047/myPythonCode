# to combine two list
num=[4,2,3,1,5]
# to sort the list item in assending order
num.sort()
print(num)

# sort in reverse order
num.sort(reverse=True)
print(num)
# or we can do like this
                            # num.reverse()
                            # print(num)

fruit=["apple","banana","orange","watermellon"]
num.extend(fruit)
print(num)
# to add new item at list last
fruit.append("gogo")
print(fruit)

# to find index of item in a list
print("index of orange is :",fruit.index("orange")) 
# to add item in a spesific place in list
fruit.insert(2,"lemon")
print(fruit)

# to remove item from the list by value we use remove 
# to remove item from the list by index we use pop
# the below example will remove value 3 from the list 
num.remove(3)
print(num)

# to remove all items from the list
                                                # fruit.clear()
                                                # print(fruit)
# to find occurence of an item in a list

print("1 comes" ,num.count(1) ,"time in this list")

# to make copy of a list

copylist=fruit.copy()
print(copylist)

# to remove value by index we use pop
print(fruit)
fruit.pop(2)
print(fruit)

# del will delete item from the list and will not return its value while pop return its value
# del is used with list dictionary and variable
list2=["khan","shan","jan","imran"]
del list2[2]
print(list2)

# del used with varaiable

x=23
del x
print(x)  #out put will be that x is not defined

# diffrence between clear and del is that del delete the complete list and
# clear delete items inside list
