import requests,json

api_url="https://api.github.com/users/hadley/orgs"

data=requests.get(api_url)
user=data.json()
print(type(user))

fp=open('new_user.json','w')
json.dump(user,fp)
print('new file is created')

fp.close()