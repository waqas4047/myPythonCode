# method 1

sentence=input("enter sentence :")
sen=sentence.split(' ')
print(sen)
capitalize_word=[word.capitalize() for word in sen]
print(capitalize_word)
capital_sen=' '.join(capitalize_word)
print(capital_sen)

# we can do above work with somple title function or mehtod

# method 2
sentence="hello this is waqas"
newsentce=sentence.title()
print(newsentce)

# method 3

sentence='hi can i go to home plx'
sen=sentence.split(' ')
print(sen)
new=[]
# capitalize_word=[word.capitalize() for word in sen]
for word in sen:
    words=word.capitalize()
    new.append(words)
print(new)
plaintet=' '.join(new)
print(plaintet)