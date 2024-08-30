'''open_file=open('countries.txt','r')
print(open_file.readline()) # will print the first line of txt fileo
open_file.close()'''



'''newfile=open('sentence.txt','r')
jon=newfile.readlines() #will print all the lines in a list each line will be pretend like individual item
print(jon)
new=''.join(jon)
print(new)'''

sentence=open('countries.txt','r')
lines=sentence.readline()
print(lines)
lines=sentence.readline()
print(lines)
lines=sentence.readline()
print(lines)


# ok=open('sentence.txt','r')
# print(ok.readlines()[0])
# ok.close()


# open_file=open('countries.txt','r')
# for files in open_file.readlines():
#     print(files)
# open_file.close()