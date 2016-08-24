import urllib2
from urllib2 import Request
import codecs
import smtplib
from bs4 import BeautifulSoup
import sys
from termcolor import colored, cprint


w,h=9,21
teamInfo = [[0 for x in range(w)] for y in range(h)]

my_url = "http://www.livescores.com/soccer/england/premier-league/"

page  = urllib2.urlopen(my_url)
soup = BeautifulSoup(page, "lxml")

team = soup.findAll("div", {"class":"team"})

pts = soup.findAll("div", {"class":"pts"})

z = 0
for x in range(0,21):
	teamInfo[x][0] = team[x].text
	for y in range(1, 9):
		teamInfo[x][y] = pts[z].text
		z+=1

#Format the print
for x in range (0, 21):
	if x == 0:
		cprint("%-*s  %s  %s  %s  %s  %s  %s  %s %s" % (20, teamInfo[x][0], teamInfo[x][1],teamInfo[x][2],teamInfo[x][3],teamInfo[x][4],teamInfo[x][5],teamInfo[x][6],teamInfo[x][7],teamInfo[x][8]),'grey')
	if x != 0 and x < 4:
		cprint("%-*s  %s  %s  %s  %s  %s  %s  %s %s" % (20, teamInfo[x][0], teamInfo[x][1],teamInfo[x][2],teamInfo[x][3],teamInfo[x][4],teamInfo[x][5],teamInfo[x][6],teamInfo[x][7],teamInfo[x][8]),'blue')
	if x == 4:
		cprint("%-*s  %s  %s  %s  %s  %s  %s  %s %s" % (20, teamInfo[x][0], teamInfo[x][1],teamInfo[x][2],teamInfo[x][3],teamInfo[x][4],teamInfo[x][5],teamInfo[x][6],teamInfo[x][7],teamInfo[x][8]),'yellow')
	if x > 17:
		cprint("%-*s  %s  %s  %s  %s  %s  %s  %s %s" % (20, teamInfo[x][0], teamInfo[x][1],teamInfo[x][2],teamInfo[x][3],teamInfo[x][4],teamInfo[x][5],teamInfo[x][6],teamInfo[x][7],teamInfo[x][8]),'red')
	if x > 4 and x <= 17:
		cprint("%-*s  %s  %s  %s  %s  %s  %s  %s %s" % (20, teamInfo[x][0], teamInfo[x][1],teamInfo[x][2],teamInfo[x][3],teamInfo[x][4],teamInfo[x][5],teamInfo[x][6],teamInfo[x][7],teamInfo[x][8]),'green')

