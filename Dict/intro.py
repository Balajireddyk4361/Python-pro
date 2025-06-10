'''
DICT::
->group of key value pairs as one entity
->duplicate keys are not allowed
->indexing is not available

'''
# Empty dict
dict={}
print(dict)

Employer={'eid':101,'esal':500000,'ename':'Balajireddy','eloc':'Bengalore'}

print(Employer)

b=Employer.keys()
print(b)

A=Employer.values()
print(A)

#using for loop iterating the keys in the Dict
for keys in Employer.keys():
    print(keys)

# using for loop fetching the values 
for values in Employer.values():
    print(values)    

# print group of key and values
for items in Employer.items() :
    print(items)
print(type(Employer))    

#Get methon 
print(Employer.get('eid'))
print(Employer['eid'])

print(Employer.get('ename'))
print(Employer.get('esal'))

