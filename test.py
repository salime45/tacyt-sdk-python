
import tacyt.TacytApp as tacytapp
import json

def test():

	api = tacytapp.TacytApp("PpQbU3AWa773ghLdf2YE", "9UWa3aqaJKrqTkYqtbyUUmyP8uT39NmUYH4HuQWJ")
	result_search = api.search_apps("links:\"http://www.emtvalencia.es\"",1 , 100, '' ,True)
		
	list = result_search.data.get('result').get('applications')
	g = result_search.data.get('result').get('numberOfGroups')

	#print (len(list))
	#print (g)

	for i in range(len(list)):
		app = list[i]
		print (app.get('title'))
		#print (app.get('apkImages'))




test()