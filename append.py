fruit=["apple","banana","orange","melon","guava","plum"]


# newlist=[]
# for x in fruit:
#     if "g" in x:
#         newlist.append(x)

# print(newlist)

                    # now i want to replace item in the list

# for x in fruit:
#     if x!="banana":
#         newlist.append(x)
#     else:
#         newlist.append("yellow")
# print(newlist)

                    # we can do this with comprehension like below

newlist=[x if x!="banana" else "Yellow" for x in fruit]
print(newlist)