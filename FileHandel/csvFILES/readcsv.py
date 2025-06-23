import csv

fp=open("emp.csv","r")
emp_csv_obj=csv.reader(fp)
'''
# print id using indexing
for emp in emp_csv_obj:
    print(emp[0])
# print names using indexing 
for emp in emp_csv_obj:
    print(emp[1])
# print sal using indexing 
for emp in emp_csv_obj:
    print(emp[2])

'''
# without an Eid,ename,esal by usin slice operator [1:]

 # without any names

for emp in list(emp_csv_obj)[1:]:
    print(emp[2])



