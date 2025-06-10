'''tuple  ()
->dulicates are allowed
->hetetogenuous are aliowed
->indexing is posible
->order maintained

'''
eids=(10,20,30,40,50,60,10,60)


print(eids.index(20))

print(eids.count(10))

print(type(eids))

for eid in eids:
    print(eid)

print(eids[6])