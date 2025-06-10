'''set {10}
->mutable
->insertion order is not maintaines
->duplicates are not allowed
->index is not maintained
->set allowed hetrogenuoes
->
----------------------------
set methods::
->set.add(10)==single element
->set.update(101,102)==multiple elements
->remove()
->discord()
->union
->intersection
->difference
->symantric difference
-->pop()
->clear()

'''

#eid={101,102,103,104,105,106,101,103,106,'Balajireddy'}
'''print(eid)

eid.add(109)
print(eid)

for eids in eid:
    print(eids)

eid.remove(105)    
print(eid)

# eid.pop()
# print(eid)

eid.update({'balaji','Reddy1'})
print(eid)
'''

#union  ="all elements in two sets"
s1={10,20,30,40,50,60}

s2={40,50,60,70,80,90}


print(s1.union(s2))
print(s2|s1)  # union method of symbal

print(s1.intersection(s2))
print(s1&s2)  # intersection method of symbal

print(s1.difference(s2))
print(s1-s2)  # - symbal

print(s2.difference(s1))
print(s2-s1)

print(s1.symmetric_difference(s2))
print(s2.symmetric_difference(s1))

print(s2^(s1))  # symmetric_difference symbal 




Enames={'balaji','ravi','ename','amulu'}

data=sorted(Enames)

print(data)
