import requests
from translate import Translator
from typing import Any, Dict, List
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import os



def restaurant(bot_handler: Any)->str:
	current_location_url = 'https://maps.googleapis.com/maps/api/geocode/json?address='
	search_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=AIzaSyDJNoEuLGP2o2PYnRWOx29AvA0kOGQJZO4&location='
	translator= Translator(to_lang="hi")
	current_location="  Triveni Sangam Allahabad"
	place = ""
	l = len(current_location)
	i=2
	while (i < l):
	    place += current_location[i] + " "
	    i = i + 1
	response = requests.get(current_location_url + place + ',+CA&key=AIzaSyAPHKNarbqTsvtUukRBx516p8KyjdCyHAM ')
	res1 = response.json()
	longi = res1["results"][0]["geometry"]["location"]["lat"]
	lati = res1["results"][0]["geometry"]["location"]["lng"]
	temp = search_url + str(longi) + ',' + str(lati) + '&rankby=distance&types=restaurant'
	response2 = requests.get(temp)
	res2 = response2.json()
	print(res2)
	i = 0
	c = 0
	ans=""
	for i in res2['results']:
	    name = i['name']
	    ans += name
	    ans += "\n"
	    #opening_hours = i['opening_hours']
	    #rating = str(i['rating'])
	    vicinity = i['vicinity']
	    ans += vicinity + "\n"
	    #rating = str(i['reviews'])    
	    #ans += rating
	    ans += "\n\n"
	    
		

	if ans == "":
	    ans = "No results"

	#translated=translator.translate(ans)
	return ans
	
def hotel(bot_handler: Any)->str:
	current_location_url = 'https://maps.googleapis.com/maps/api/geocode/json?address='
	search_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=AIzaSyDJNoEuLGP2o2PYnRWOx29AvA0kOGQJZO4&location='
	translator= Translator(to_lang="hi")
	current_location="  Triveni Sangam Allahabad"
	place = ""
	l = len(current_location)
	i=2
	while (i < l):
	    place += current_location[i] + " "
	    i = i + 1
	response = requests.get(current_location_url + place + ',+CA&key=AIzaSyAPHKNarbqTsvtUukRBx516p8KyjdCyHAM ')
	res1 = response.json()
	longi = res1["results"][0]["geometry"]["location"]["lat"]
	lati = res1["results"][0]["geometry"]["location"]["lng"]
	temp = search_url + str(longi) + ',' + str(lati) + '&rankby=distance&types=lodging'
	response2 = requests.get(temp)
	res2 = response2.json()
	print(res2)
	i = 0
	c = 0
	ans=""
	for i in res2['results']:
	    name = i['name']
	    ans += name
	    ans += "\n"
	    #opening_hours = i['opening_hours']
	    #rating = str(i['rating'])
	    vicinity = i['vicinity']
	    ans += vicinity + "\n"
	    #rating = str(i['reviews'])    
	    #ans += rating
	    ans += "\n\n"
	    
		

	if ans == "":
	    ans = "No results"

	#translated=translator.translate(ans)
	return ans

