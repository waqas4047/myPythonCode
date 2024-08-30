student={
    'waqas':{'name':'waqas','age':43,'gender':'male'},
    'qiser':{'name':'qiser','age':23,'gender':'male'},
    'izhar':{'name':'izhar','age':98,'gender':'male'},
    'kamran':{'name':'kamran','age':12,'gender':'male'},
}

student.update({'jan':{'name':'jan','age':55,'gender':'male'}})
for students in student.values():
    if students['gender']=='male':
        print(students)