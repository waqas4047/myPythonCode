# casefold is used for comparisn if both text is same it will give match else will give unmatch
string1="hello this is my new text"
string2="Hello this Is my new text"
# string3=string2.strip()
# print(string3)
if string1.casefold()==string2.casefold():
    print("matched")
else:
    print("unmatched")