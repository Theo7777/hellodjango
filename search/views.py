from django.http import HttpResponse
from django.shortcuts import render
import json
import requests
from bs4 import BeautifulSoup
import lxml
import re
from twitter import *


#Espn API Information
url ='http://api.espn.com/v1/sports/soccer/eng.1/athletes?offset='
espn_api_key = 'grs2svvgyfbnuacue8ztu6ca'
# (url + '&apikey=' + api_key)

# #Twitter API Information
CONSUMER_KEY="ttBogoGdBF14y20tmjikIQ"
CONSUMER_SECRET="RUd0kRTcOefJ2iEK5JzU0Z1s0dMLVWxtxbYz7hDGiJw"
OUTH_TOKEN="116472192-tGRKctDKoRpivGxmHHK5EOAWL68iT6vRZOpkBH70"
OAUTH_SECRET="PulgU7g4Mb4UXBYVbrHr1k1ZXey4nVX1fL8uP2wgycM"

t = Twitter(auth = OAuth(OUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

#skysports Newspaper Information
sky_sports_url ='http://www1.skysports.com/transfer-centre/papertalk'


def search_form(request):
    return render(request, 'new-search.html')


def search(request):
	#checking if query was made 
	if 'q' not in request.GET:
		error = []
		error.append('You did not enter a query, please try again!')
		return 	render(request, 'new-search.html', {'error':error})
	elif 'q' in request.GET:
		n = request.GET['q']
		name = n.title()
		offset = -50
		for num in range(13):
			offset += 50
			response = requests.get(url + str(offset) + '&apikey=' + espn_api_key)
			data = json.loads(response.content)
			try:				
				players = data["sports"][0]["leagues"][0]["athletes"]
				n = -1
				for names in players:
					player_name = players[n]['fullName']
					if name in player_name:
						details = players[n]					
						link = details['links']['web']['athletes']['href']
						profile_response = requests.get(link)
						profile_data = profile_response.content
						soup = BeautifulSoup(profile_data, 'lxml')
						profile = soup.find('ul', {'class':'profile-items'}).findAll('li')
						#stats = soup.find('table', {'class':'feat-stats-table'}).findAll('td')
						#stats_items = []
						profile_items =[]
						for items in profile:
						 	profile_items.append(items.string)
						#for statistics in stats:
						#	stats_items.append(statistics.string) 
						profile_pic = soup.find('div', {'class':'player-photo'}).find('img')
						image = profile_pic.get('src')
						n += 1
						#return HttpResponse('ok')
					else:
						n += 1
			except:
				players = data.sports[0].leagues.[0]athletes
				n = -1
				for names in players:
					player_name = players[n]['fullName']
					if name in player_name:
						details = players[n]					
						link = details['links']['web']['athletes']['href']
						profile_response = requests.get(link)
						profile_data = profile_response.content
						soup = BeautifulSoup(profile_data, 'lxml')
						profile = soup.find('ul', {'class':'profile-items'}).findAll('li')
						#stats = soup.find('table', {'class':'feat-stats-table'}).findAll('td')
						#stats_items = []
						profile_items =[]
						for items in profile:
						 	profile_items.append(items.string)
						#for statistics in stats:
						#	stats_items.append(statistics.string) 
						profile_pic = soup.find('div', {'class':'player-photo'}).find('img')
						image = profile_pic.get('src')
						n += 1
						#return HttpResponse('ok')
					else:
						n += 1

		#twitter search
		tweets = t.search.tweets(q=details['fullName'], lang='en')
		results = []
		for i in tweets['statuses']:
			results.append(i['text'])			

		return render(request, 'success1.html', {'details':details,  'profile':profile_items, 'results':results,'image':image })
					# gossip_response = requests.get(sky_sports_url)
					# gossip_data = gossip_response.content
					# gossip_soup = BeautifulSoup(gossip_data, 'lxml')

					#if gossip_soup.find(text=re.compile(player_name)):
					# 	gossip_text = gossip_soup.find(text=re.compile(player_name))
					# 	gp = gossip_text.findPrevious('img').get('alt')
					# 	gossip_newspaper = gp.title()
					# else:			
					# 	no_gossip = []
					# 	no_gossip.append('no')
					# 	n += 1
					# 	results = api.search(name)
					# 	return render(request, 'success1.html', {'details':details, 'results':results, 'profile':profile_items, 'image':image, 'no_gossip':no_gossip})

# (url + '&apikey=' + api_key)


