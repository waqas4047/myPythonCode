var1 = 12
var2 = 39
var3 = 36
var4 = 77
while(1):
    num = int(input("Enter a number: "))
    count=0
    if num==0:
        print("false")
    elif num!=0:    
        if var1 % num == 0:
            count += 1

        if var2 % num == 0:
            count += 1
        if var3 % num == 0:
            count += 1
        if var4 % num == 0:
            count +=1
        # Print the result
        print(f"{count} value are divisible by {num}")
