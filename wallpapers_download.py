#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
from StringIO import StringIO
from lxml import etree

def download_image(image_url, local_folder, folder_index):
	ufile = urllib2.urlopen(image_url)
	root = etree.parse(ufile, etree.HTMLParser())
	dwnld =  root.xpath('//div[@class="wallpaper_big"]//div[@class="wb_preview"]//a//img/@src')
	f = open(local_folder + "/" + str(folder_index)+".jpg", 'wb')
	f.write(urllib2.urlopen("http:"+dwnld[0]).read())
	f.close()

def retrieve_image_direct_links(query, page_idx, links_accum):
	page_str = ""
	if page_idx >= 2:
		page_str = "/page" + str(page_idx)
	url = "https://wallpaperscraft.com/search/keywords?q=" + query + page_str
	ufile = urllib2.urlopen(url)
	root = etree.parse(ufile, etree.HTMLParser())
	for entry in root.xpath('//div[@class="wallpaper_pre"]//a/@href'):
		links_accum.append("https:"+entry)

my_queries = ["forest", "river", "bike", "warmth", "sun", "game", "rain", "fish", 
				"sea", "travel", "city", "wheel", "train", "bridge", "skirt"]

def main():
	image_page_links = []
	for mq in my_queries:
		for p in range(1, 20):
			retrieve_image_direct_links(mq, p, image_page_links)
	
	i = 0
	image_file_links = []
	for al in image_page_links:
		download_image(al, "/home/olia/Pictures", i)
		i = i+1

if __name__ == '__main__':
	main()