 class info():
...     def __init__(self, firstName, lastName):
...             self.firstName = firstName
...             self.lastName = lastName
... 
>>> def search_espn():
...     search_url = 'http://api.espn.com/v1/sports/soccer/eng.1/athletes?offset='
...     api_key = 'grs2svvgyfbnuacue8ztu6ca'
...     url = 'http://api.espn.com/v1/sports/soccer/eng.1/athletes?offset='
...     search_url = url + '&apikey=' + api_key
...     import simplejson as json
...     import urllib
...     raw = urllib.urlopen(search_url)
...     js = raw.readlines()
...     js_object = json.loads(js[0])
...     results = []


def look():
	name = raw_input()
	offset = -50
	for num in range(12):
		offset += 50
		req = urllib2.Request(url + str(offset) + '&apikey=' + api_key)
		response = urllib2.urlopen(req)
		data = response.read()
		players = data['sports'][0]['leagues'][0]['athletes']
		n = 0
		for names in players:
			if players[n]['lastName'] == name:
				print 'My name is ' + name + '. See my details below'
				pprint.pprint(players[n])
				n += 1
			else:
				n += 1

def getPage():
	api_key = 'grs2svvgyfbnuacue8ztu6ca'
	url = 'http://api.espn.com/v1/sports/soccer/eng.1/athletes?offset='
	search_url = url + '&apikey=' + api_key

	req = urllib2.Request(url + str(offset) + '&apikey=' + api_key)
	response = urllib2.urlopen(req)
	return response.read()