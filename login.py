print("Create your account :")

username1=input("Enter your User Name :")
passwd1=input("Enter your Password:")
print("****************Log IN*******************")

flag= True
while flag:
    username2=input("Enter your User Name :")
    passwd2=input("Enter your Password:")

    if username1==username2 and passwd1==passwd2:
        print("You Loged successfully")
        flag= False
    else:
        print("*********************Try agian************************")    