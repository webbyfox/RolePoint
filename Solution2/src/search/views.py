from django.shortcuts import render, HttpResponse
import json,os
# from pprint import pprint

# Create your views here.
def index(request):
	result = []
	# for key,value in dir(get_json_data()).item():
		# result.append(value)
	return HttpResponse(str(type(get_json_data())))

def get_json_data():
	app_dir = os.path.dirname(os.path.abspath(__file__))
	with open(app_dir + '/data.json') as data_file:    
		data = json.load(data_file)
	return data

def search(q):
	pass
