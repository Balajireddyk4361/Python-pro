emplpoyees=[{"id":1,"first_name":"Rikki","gender":"Female","country":"Paris"},
{"id":2,"first_name":"Olav","gender":"Male","country":"Vienna"},
{"id":3,"first_name":"Lyman","gender":"Male","country":"Dubai"},
{"id":4,"first_name":"Mirabelle","gender":"Female","country":"Paris"},
{"id":5,"first_name":"Celestina","gender":"Female","country":"Atlanta"},
{"id":6,"first_name":"Cortie","gender":"Male","country":"Hong Kong"},
{"id":7,"first_name":"Cassie","gender":"Female","country":"Copenhagen"},
{"id":8,"first_name":"Joane","gender":"Female","country":"Paris"},
{"id":9,"first_name":"Wallie","gender":"Female","country":"Paris"},
{"id":10,"first_name":"Gretta","gender":"Female","country":"Singapore"}]
# Dont use the filter 
male_epm=[]

for emp in emplpoyees:
    if emp['gender'] == 'Female':
        male_epm.append(emp)


print(len(male_epm))

# --------------------------------------------------------------------
# using the filter
def check_gender(emp):
    return emp['gender'] == "Female"

Female_emp=list(filter(check_gender,emplpoyees))

print(len(Female_emp))
#----------------------------------------------------------------------------

print(len(list(filter(lambda empployees:emplpoyees['gender']=="Male"))))