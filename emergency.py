
import requests
from translate import Translator
from typing import Any, Dict, List
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import os



def hospital(bot_handler: Any)->str:
	current_location_url = 'https://maps.googleapis.com/maps/api/geocode/json?address='
	search_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=AIzaSyAPHKNarbqTsvtUukRBx516p8KyjdCyHAM &location='
	translator= Translator(to_lang="hi")
	current_location="  Triveni Sangam Allahabad"
	place = ""
	l = len(current_location)
	i=2
	while (i < l):
	    place += current_location[i] + " "
	    i = i + 1
	#print(place)
	r = requests.get(current_location_url + place + ',+CA&key=AIzaSyBKmBYERZyz9Cj7-F9bT7WMWVuSHiaX9kU')
	results = r.json()
	#print(results)
	longi = results["results"][0]["geometry"]["location"]["lat"]
	lati = results["results"][0]["geometry"]["location"]["lng"]

	temp = search_url + str(longi) + ',' + str(lati) + '&rankby=distance&types=hospital'
	response = requests.get(temp)
	result = response.json()
	#print(result)
	i = 0
	ans=""
	translated=""
	for i in result['results']:
	    name = i['name']
	    temp = name
	    temp += "\n"    
	    vicinity = i['vicinity']
	    temp += vicinity   
	    temp += "\n\n"
	    ans += temp
	    #int_trans = translator.translate(temp)
	    #translated += int_trans


	if ans == "":
	    ans = "No results"
	    #translated = translator.translate(ans)
	#ans += translated
	return ans
    
def contacts(bot_handler: Any)->str:

	emergency_url="https://kumbh.gov.in/en/emergency-services"
	uClient=uReq(my_url)
	page_html=uClient.read()
	uClient.close()
	translator= Translator(to_lang="hi")

	page_soup=soup(page_html,"html.parser")
	containers=page_soup.findAll("div",{"class":"align-left"})
	container=containers[2]
	p=container.text
	ans = os.linesep.join([s for s in p.splitlines() if s])
	#print(ans)
	#container=containers[0]

	#ans=container.text
	#translated=translator.translate(ans)
	return ans



