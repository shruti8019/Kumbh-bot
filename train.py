import sys, os, zulip
sys.path.insert(0,os.getcwd())
import codecs
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from translate import Translator
import json
from typing import Any,List,Dict
import datetime
from dateutil.relativedelta import relativedelta

def live_station(bot_handler: Any, *params ) -> str:
	#content = message["content"]
	#words = content.split()
	api_key="<YOUR RAILWAY API KEY>" 
	translator= Translator(to_lang="hi")
	train_number=params[0]
	station_code="ALD"
	print(type(params))
	print("train Number : " + str(train_number))
	string = ''.join(params)
	print("string : " + string)
	one_year_from_now = datetime.datetime.now() + relativedelta(years=1)
	current_date = datetime.datetime.now().strftime("%d-%m-%Y")
	#print(current_date)
	base_url = "https://api.railwayapi.com/v2/live/train/"+train_number+"/station/"+station_code+"/date/"+current_date+"/apikey/"+api_key+"/"
	j=uReq(base_url)
	#print(base_url)
	
	reader = codecs.getreader("utf-8")
	data = json.load(reader(j))
	x=data['status']
	ans=""
	ans +="Scheduled departure:" + x['schdep'] + "\n" + "Actual Arrival:"+ x['actarr'] + "\n"+"Scheduled arrival:" +x['scharr'] +"\nActual 		arrival:" +x['actarr'] + "\n"
	#translated=translator.translate(ans)
	#translated1=translator.translate(data['position'])
	ans+=("\n" + data['position']+"\n")
	return ans


#https://api.railwayapi.com/v2/live/train/<train-number>/station/<station-code>/date/<dd-mm-yyyy>/apikey/<apikey>/

def train_route( bot_handler: Any, *params) -> str:
	
	api_key="<YOUR RAILWAY API KEY>" 
	train_number=params[0]
	train_n=''.join(params)
	print("Train number= " + train_n)
	base_url = "https://api.railwayapi.com/v2/route/train/"+train_n+"/apikey/"+api_key+"/"
	j=uReq(base_url)
	print(base_url)
	reader = codecs.getreader("utf-8")
	
	data = json.load(reader(j))
	ans=""
	for station in data['route']:
            s=station['station']	
            ans+=s['name']+"\t"+station['schdep']+"\t"+station['scharr']+"\n"
	#translated=translator.translate(ans)
	ans+=(ans + "\n")
	return ans

	

#https://api.railwayapi.com/v2/route/train/<train number>/apikey/<apikey>/


