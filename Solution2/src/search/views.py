from django.shortcuts import render, HttpResponse
import json,os

from django.http import HttpResponseRedirect

def search_page(request):
		return render(request, 'search/index.html', {'data':get_json_data()})
	
def get_json_data():
	app_dir = os.path.dirname(os.path.abspath(__file__))
	with open(app_dir + '/data.json') as data_file:    
		data = json.load(data_file)
	return data

def search(request, query):
	result =  [item for item in get_json_data() if query.lower() in item['name'].lower() 
												or query.lower() in item['company'].lower()]
	return render(request, 'search/index.html', {'data':result})

def get_query(request):
	if request.method =='GET':
		 query = request.GET.get('query','')
		 return HttpResponseRedirect('/search/' + str(query) + '/')