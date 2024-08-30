import random   # here we added a random library
mylist=[23,54,67,76,82,12,11,25,68,95,90,80,75,88,33,51]
new=[]    # empty list
i=1
while(i<=5): # we want to add 5 number from the mylist to new list
    rand_num= random.choice(mylist) # here we use choice to select random element form the list tuple or stirng
    print(rand_num)
    new.append(rand_num)
    i=i+1
print(new)

# now using random.sample
randlist=random.sample(mylist,5) #if we want to pic 5 value from my list and want to make new list of 
# random number so this is the best approch and if we want single value from list then the above is good mehtod
print(randlist)  



# random.choice():

# 1. Selects a single random element from the list.
# 2. Can select the same element multiple times (replacement).
# 3. Returns a single element, not a list.

# random.sample():

# 1. Selects multiple random elements from the list.
# 2. Ensures unique elements (no replacement).
# 3. Returns a list of selected elements.
