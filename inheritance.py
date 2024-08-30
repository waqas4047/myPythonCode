from inher_demo.inheritance_d import myclass # with the help of this we can import class from other file

class person(myclass): # now we can access data of myclass here
    pass

p1=person()

print(person.name)

#from demo.demo_class import MyClass

#with help of above method we can inherit class from another directory name demo inside file name is demo_class which contain 
#class name myclass