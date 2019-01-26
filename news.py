

import sys, os, zulip
sys.path.insert(0,os.getcwd())

from wit import Wit
from typing import Any, Dict

import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

def getHeadline(bot_handler: Any)->str:
	news_url="https://news.google.com/news/rss"
	Client=urlopen(news_url)
	xml_page=Client.read()
	Client.close()

	soup_page=soup(xml_page,"xml")
	news_list=soup_page.findAll("item")
	headlines=""
	for news in news_list:
		headlines += news.title.text + "\n"
		headlines += news.link.text + "\n"
		headlines += news.pubDate.text + "\n"
		headlines += news.pubDate.text + "\n"
		headlines += "\n\n\n"
	return headlines
		
		
		
		
		
		
		
		
