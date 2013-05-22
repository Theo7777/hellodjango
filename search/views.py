from django.http import HttpResponse
from django.shortcuts import render
import json
import requests
import pprint
import tweepy


#Espn API Information
url ='http://api.espn.com/v1/sports/soccer/eng.1/athletes?offset='

espn_api_key = 'grs2svvgyfbnuacue8ztu6ca'

#Twitter API Information
consumer_key="ttBogoGdBF14y20tmjikIQ"
consumer_secret="RUd0kRTcOefJ2iEK5JzU0Z1s0dMLVWxtxbYz7hDGiJw"
access_token="116472192-tGRKctDKoRpivGxmHHK5EOAWL68iT6vRZOpkBH70"
access_token_secret="PulgU7g4Mb4UXBYVbrHr1k1ZXey4nVX1fL8uP2wgycM"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def search_form(request):
    return render(request, 'search_form.html')


# def search(request):
#     if 'q' in request.GET:
#         message = 'You searched for: %r' % request.GET['q']
#     else:
#         message = 'You submitted an empty form.'
#     return HttpResponse(message)


def search(request):
	if 'q' in request.GET:
		name = request.GET['q']
		name = name.title()
		offset = -50
		for num in range(13):
			offset += 50
			response = requests.get(url + str(offset) + '&apikey=' + espn_api_key)
			data = json.loads(response.content)
			players = data["sports"][0]["leagues"][0]["athletes"]
			n = -1
			for names in players:
				if name in players[n]['fullName']:
					#print 'My name is ' + name + '. See my details below'
					details = players[n]
					n += 1
					#return HttpResponse('ok')
				else:
					n += 1

#twitter search
		results = api.search(name)
		return render(request, 'success1.html', {'details':details, 'results':results})


		


				

 # def search():
 # 	name = raw_input()
 # 	name = name.title
 # 	return look(name)


	# if request.method == 'POST':
	# 	if name == POST['name']:
	# 		name = POST['name']
	# 		name = name.title()
	# 		return look(name)
	# (url + '&apikey=' + api_key)

