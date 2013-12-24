#!/usr/bin/python2.7 -tt

import sys
import urllib, urllib2
import requests

def gotrobots(site):
	robotsite = site + '/robots.txt'
	response = requests.get(robotsite)
	if response.status_code == 200:
	    getrobots(site)
	else:
	  print "No robots.txt"

def getrobots(site):
	robotsite = site + '/robots.txt'
	response = urllib2.urlopen(robotsite)
	html = response.read()

	with open('robots.txt', 'w') as f:
	    f.write(html)

	robots = open("robots.txt")
	robots_length = len(open('robots.txt','r').read().split('\n'))

	for i in range(1,robots_length):
	    read = robots.readline()
	    path = read.split(':')

	    if path[0] == "Disallow":
	        disallow = path[1].split("\n")
	        dir = disallow[0].lstrip()
	        disurl = site + dir
	        resp = requests.get(disurl)
	        print str(resp.status_code) + " : " + disurl

	robots.close()

def main():
    if len(sys.argv) >= 2:
        gotrobots(sys.argv[1])

if __name__ == '__main__':
	main()
