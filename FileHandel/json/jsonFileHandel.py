'''
json
------------------
loads:convert json to python
dumps:convert python to json 
load: if you wants to dump python data intop json file
dump:if you want to read json file and convert to python data
'''
import json
emp={
    'eid':101,
    'esal':90000,
    'ename':'Balajireddy',
    'loc':True,
    'type':None
}
print(type(emp))
employee=json.dumps(emp)

print(employee)
print(type(employee))
'''out put
<class 'dict'>
{"eid": 101, "esal": 90000, "ename": "Balajireddy", "loc": true, "type": null}
<class 'str'>
'''
