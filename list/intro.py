''' 1) group of elements as one entity
    ->allowed duplictes
    ->allowed heterogenuoes element
    -> indexing is posible
    ->-ve index also posiple
    ->list is a literavle abject 
'''
# crud operations in list 
fruits=['banana','orange','apple','grapes']
Names=['Balaji','Rededy','samba','raghava']

# print(fruits[0])
# print(Names[3])

# for Name in fruits:
#     print(Name)


# i=0
# while i<=len(fruits)-1:
#     print(fruits[i])
#     i=i+1

 
''' delete methods  
  ->list.clear
  ->list.pop
  ->list.remove
------------------------------
   update methods
   ->list.extend()
   ->list.append()
   ->lis.insert()
   ->list.short()
   ->list.reverse()
--------------------------------
    read mthods
    ->list.index()
    ->list.count()
'''    
# Names=['balaji','Reddy''shannu','fans','raghus','balaji']

# print(Names.index('raghus'))
# print(Names[0])
# print(Names.count('balaji'))


enames=['rg','sg','pg','rg']
# print(enames[3])
# enames.append('Balaji')
# print(enames)

# print(enames.index('rg'))

'''
----------------------------------
insert method
'''
enames.insert(3,'Balaji')
print(enames)

enames.reverse()
print(enames)

enames.sort()
print(enames)

enames.remove('rg')
print(enames)

print(enames.pop())
print(enames)

enames.sort(reverse=True)
print(enames)

enames.extend('balaji')
print(enames)



