student={
    'waqas':{'name':'waqas','age':43,'gender':'male','favrite_sub':'eng'},
    'qiser':{'name':'qiser','age':23,'gender':'male','favrite_sub':'math'},
    'izhar':{'name':'izhar','age':98,'gender':'male','favrite_sub':'urdu'},
    'kamran':{'name':'kamran','age':12,'gender':'male','favrite_sub':'islam'},
}
# to print fav_sub of all students
for students in student.values():
    print( f'fav_sub of : {students['name']} is {students['favrite_sub']}')

# update age of student waqas
student['waqas']['age']=55


# making function to add student to the above dictionary

def add_student(name,age,gender,fav_sub):
    student.update({name:{'name':name,'age':age,'gende':gender,'favrite_sub':fav_sub}})
add_student('shan',44,'female','psycology')
add_student('tuba',33,'transe','arbi')


# to print all the keys and studnet of a dictionary inside disctioru

for student , detail in student.items():
    print("\n\n")
    print(f"student : {student}")
    for key , value in detail.items():
        print(f'{key} : {value}')



