def greeting():
    print("hello this coding for function")
greeting()

# parametrized function
                                        # value1=int(input("enter first num :"))
                                        # value2=int(input("enter second num :"))
                                        # def add(a,b):
                                        #     print(f"the sum of {a} and {b} is {a + b}")
                                        # add(value1,value2)



# if we dont know how many values we are passing then we can write code like this
def greet(*name):
    print("welcome mr ", name[0][1]) # then we will enter the index of value
    print(type(name)) 
greet(("waqas","qaiser","izhar"),("shan")) #here we have pass two tuples


# passing tuple into function
tuple1=("hello","new","shan")
tuple2=("can","man","jan")
# we can use staric and one varible for to many arguments 
def new(*parmeter): #it will devide the comming parameters into indexes
    print(parmeter[0])
new(tuple1,tuple2)