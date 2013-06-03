from django.http import HttpResponse
from django.shortcuts import render
import json
import requests
import tweepy
from bs4 import BeautifulSoup
import lxml
import re


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

#skysports Newspaper Information
sky_sports_url ='http://www1.skysports.com/transfer-centre/papertalk'


def search_form(request):
    return render(request, 'new-search.html')


# def search(request):
#     if 'q' in request.GET:
#         message = 'You searched for: %r' % request.GET['q']
#     else:
#         message = 'You submitted an empty form.'
#     return HttpResponse(message)


def search(request):
	if 'q' in request.GET:
		n = request.GET['q']
		name = n.title()
		offset = -50
		for num in range(13):
			offset += 50
			response = requests.get(url + str(offset) + '&apikey=' + espn_api_key)
			data = json.loads(response.content)
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
					profile_items =[]
					for items in profile:
					 	profile_items.append(items.string)
					profile_pic = soup.find('div', {'class':'player-photo'}).find('img')
					image = profile_pic.get('src')
					n += 1
					#return HttpResponse('ok')
				else:
					n += 1

#twitter search
		results = api.search(name)
		return render(request, 'success1.html', {'details':details, 'results':results, 'profile':profile_items, 'image':image })

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

