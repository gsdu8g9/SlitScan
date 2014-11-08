#!/usr/bin/python

from Harvester import WebParser

url       = "http://proxy-list.org/english/index.php?p=%d"
regex     = r'\<li class\=\"proxy\"\>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\:(\d{2,5})\</li\>'
pages     = 10

wp = WebParser(url,regex,pages)
for remote in wp.remotes():
	wp.scan(remote)
