class person:
    def __init__(self,name,age):
        self.namee=name
        self.agee=age


name=input("enter your name")
age=input("enter your age")

obj=person(name,age)
print(obj.namee)

# we can delete property from the class like this
del obj.agee  # it will give arror that object has no attribute agee
print(obj.agee)

# we can also delete whole object like below

# del obj