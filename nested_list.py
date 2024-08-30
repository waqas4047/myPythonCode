mylist=[
    [1,2,3,4,5],
    [6,7,8,9,10]
]

# i want ot print in list 1 value no 3
print(mylist[0][2])
print('list 2')
for items in mylist[1]:
    print(items)

#nested loop

mylist=[
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
]

print("print all the items of nested list using nested loop")
# for accesing all the list inside list
for lists in mylist:
    # for accesing items inside list
    for items in lists:
        print(items)
