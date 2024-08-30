# a=23
# b=55
# if a<b:
#     print("a is less then b")
# else:
#     print("b is less than a")


# c=True
# d=False
# if c==True or d==True: #will execute its value when one of the both condetion is true
#     print("one of the above condition is true")
# else:
#     print("both conditions are false")


# e=True
# f=False
# if e==True and f==True: #will execute its value when both condetions are true
#     print("both condition are true")
# else:
#     print("one of the condition is false")

# # find type 

# value=(input("enter value :"))

# if type(value)==str:
#     print(value +" is string")
# elif type(value)==int:
#     print(value ,"  is integer")
# else:
#     print("other data type")

# num=int(input("enter the number to check wether the number is multiple of 5 or not"))

# if num%5==0:
#     print("the number is divisible by 5")
# else:
#     print("not divisible")


bio_data={
    "waqas_bio_data":{
        "name":"waqas",
        "age":43,
        "country":"pakistan"
    },
    "shan_bio_data":{
        "name2":"waqas",
        "age":43,
        "country":"india"
    },
    "jan_bio_data":{
     "name3":"waqas",
    "age":43,
    "country":"pakistan"
    }
}


new=[]
for x in bio_data.values():
    print(x)
    if x['country']=='pakistan':
        new.append(x)

print(new)
