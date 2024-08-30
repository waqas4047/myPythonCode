'''try:
    x=int(input("enter an integer : "))
    print(x)

except:
    print("value not an integer")'''

# value error
#  if system want integer and u enter string then we can trough value error like bellow
'''
try:
    x=int(input("enter an integer : "))
except ValueError:
    print("value error")
else:
    print("there is no error")
'''

# after finishing try and axcept
try:
    x=int(input("enter an integer : "))
except:
    print("some thing went wrong")
finally:
    print("try and except is finished")
