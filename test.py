
import tacyt.TacytApp as tacytapp
import json

def getApps():

	api = tacytapp.TacytApp("PpQbU3AWa773ghLdf2YE", "9UWa3aqaJKrqTkYqtbyUUmyP8uT39NmUYH4HuQWJ")
	result_search = api.search_apps("links:\"http://www.emtvalencia.es\"",1 , 100, '' ,True)
		
	list = result_search.data.get('result').get('applications')
	g = result_search.data.get('result').get('numberOfGroups')

	#print (len(list))
	#print (g)

	for i in range(len(list)):
		app = list[i]
		print (app.get('title'))


def getRss():

	api = tacytapp.TacytApp("PpQbU3AWa773ghLdf2YE", "9UWa3aqaJKrqTkYqtbyUUmyP8uT39NmUYH4HuQWJ")
		
	result = api.get_RSS_info('56cd790de4b03cbf45a334b8')

	print (result.data)
		
def getFilters():

	api = tacytapp.TacytApp("PpQbU3AWa773ghLdf2YE", "9UWa3aqaJKrqTkYqtbyUUmyP8uT39NmUYH4HuQWJ")
		
	result = api.read_all_filters()
	list = result.data.get('result').get('filters')

	print (len(list))
	for i in range(len(list)):
		app = list[i]
		print (str(app) + "\n")
		
getFilters()