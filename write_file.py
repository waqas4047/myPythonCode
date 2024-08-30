# hello=open('new.txt','w') # with the help of this we can crate new file  in write mood
# hello.write("hello this is my new file") # with the help of this we can write some thing in file 

# we give name of an exixting file in the above open("new.txt") if we write name of existing file in place of
# new.tx then it will orride all the things which is presingt in that file

# it will override the text which is present in sentence.txt 
new=open('sentence.txt','w')
new.write("ok go to home")

# if i want to add new text to an existing text then i will use a in place of above 'w'

# now i want to append text to a doucment
app=open('countries.txt','a')
app.write('\n hello tis is cristiano runaldo')  #\n is used for to start form new line
app.close()
