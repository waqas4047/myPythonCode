student={
    'waqas':{'name':'waqas','age':43,'gender':'male','favrite_sub':'eng'},
    'qiser':{'name':'qiser','age':23,'gender':'male','favrite_sub':'math'},
    'izhar':{'name':'izhar','age':98,'gender':'male','favrite_sub':'urdu'},
    'kamran':{'name':'kamran','age':12,'gender':'male','favrite_sub':'islam'},
}

# delete student of record 
del student['waqas']


# we can also delete like

student.pop('kamran')

for students in student.values():
    print(students)