# read

import json

fp=open('emp.json','r')

emp=json.load(fp)

print(emp)
for employees in emp:
    print(employees['ename'])