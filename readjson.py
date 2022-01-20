# readjson.py


import json

def readjson():
	with open('data.json', encoding='utf-8') as file:
		data = json.load(file)
		print(type(data))
		print(data[0])
		print(data[1])
	return data

readjson()

def writejson(data):
	jsonobject = json.dumps(data, ensure_ascii  = False)
	with open('fruit.json','w',encoding = 'utf-8') as file:
		file.write(jsonobject)

data = {'1234441133':['Banana',100,5],
		'1234415133':['แตงโม',174,99],
		'1234941133':['แก้วมังกร',789,5]}

writejson(data)