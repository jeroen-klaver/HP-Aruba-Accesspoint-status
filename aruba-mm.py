import requests
import json
from pprint import pprint
import urllib3

# Surpress error messages for controllers without SSL certificates
#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


#login
url = "https://192.168.100.2:4343/v1/api/login"

payload={'username': 'admin',
'password': 'admin'}
files=[

]
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

logindata = response.json()
message = logindata['_global_result']["status_str"]
token = logindata['_global_result']['X-CSRF-Token']
uid = logindata['_global_result']['UIDARUBA']
cookies = {'SESSION': uid}

# GET API to retrieve accesspoint status
print("Retreiving show ap-database-summary \n")
url = ("https://192.168.100.2:4343/v1/configuration/showcommand?command=show ap database-summary&UIDARUBA=" +uid)

payload={}
files={}
headers = {
  'Cookie': '(null); SESSION=' +uid 
}

response = requests.request("GET", url, headers=headers, data=payload, files=files)

print(response.text)

#Wait 5 seconds
import time
time.sleep(5)


#Logout. Otherswise error: WebUI session limit reached
url = ("https://192.168.100.2:4343/v1/api/logout")
payload={}
files={}
headers = {
  'Cookie': '(null); SESSION=' +uid 
}
