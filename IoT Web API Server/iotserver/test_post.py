import requests


def post_data(data):
    url = 'http://127.0.0.1:8000//api'
    r = requests.post(url=url, json=data)
    print(r.text)


# data = {"code": "TM-1004",
#         "title": "Check Smart Home Humid",
#         "temperature": "32.80",
#         "humidity": "78.00"}
# post_data(data)

def post_get_sensor_data(CODE):
	# url = 'http://192.168.0.100:8000/api'
	url = 'http://127.0.0.1:8000/sensor-current-multiple-post/{}'.format(CODE)
	data = {'token':'xyz123'}
	r = requests.post(url=url,data=data)
	print(r.text)


post_get_sensor_data('TM-1001')
