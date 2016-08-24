#Live EPL Score from Past 7 Days

import urllib2
from urllib2 import Request
import codecs
import smtplib
from bs4 import BeautifulSoup
import sys
from termcolor import colored, cprint


length = 50
resultInfo = [0 for x in range(length)]

my_url = "http://www.livescores.com/soccer/england/premier-league/results/7-days/"

page  = urllib2.urlopen(my_url)
soup = BeautifulSoup(page, "lxml")

game = soup.findAll("div", {"class":"row-gray"})

x = 0
for x in range(0, 50):
	try:
		resultInfo[x] = game[x].text
		print resultInfo[x]
	except:
		break

	
	