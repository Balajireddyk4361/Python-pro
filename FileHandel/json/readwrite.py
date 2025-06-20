import json

fp1=open('emp.json','r')
fp2=open('user.json','w')

user=json.load(fp1)
print(type("user"))

json.dumps(user,fp2)

