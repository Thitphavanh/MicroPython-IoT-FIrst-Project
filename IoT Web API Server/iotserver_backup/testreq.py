import requests
# pip install requests
'''
code
name
temperature
humidity
'''

url = 'http://192.168.0.100:8000/sensor-post'
data = {'code': 'TM-101','name':'Temp and Humid - 1','temperature':30.50, 'humidity':50.3}

r = requests.post(url, json = data)
print(r)