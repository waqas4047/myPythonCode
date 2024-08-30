string="hello this is a great good part of my life its supper cool so its going well it also go fowrward \
    so now going well so it is very good opertunity it is like a good man so be fast to get you \
        experience it is good going well it now i am going to good home so be fast"

while(1):
    insstring=input("enter your string\n")

    countstring=string.count(insstring)

    print("this world is " ,countstring,"time in the string")

    if(countstring>=3):
        print("blue")
    elif(countstring==2):
        print("green")
    elif(countstring==1):
        print("red")
    else:
        print("this word does't exist in this string")