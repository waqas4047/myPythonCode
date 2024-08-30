num1=int(input("enter your first number :"))
num2=int(input("enter your scond number"))
op=input("enter operator : ")

if op=='+':
    print(f"the addition of {num1} and {num2} is {num1+num2}")
elif op=='-':
    print(f"the subtraction of {num1} and {num2} is {num1-num2}")
elif op=='*':
    print(f"the multiplication of {num1} and {num2} is {num1*num2}")
elif op=='/':
    print(f"the division of {num1} and {num2} is {num1/num2}")
else:
    print("incorect operator")