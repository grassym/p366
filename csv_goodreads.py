#!/usr/bin/env python

import csv

goodreads_library_export_path = "files/goodreads_library_export.csv"

def find_exclusive_shelf_field_index(csv_row):
	index = 0
	for item in csv_row:
		if (item == "Exclusive Shelf"):
			return index 
		index += 1
	return -1

def main():
	file_search_list = []
	with open(goodreads_library_export_path) as csvfile:
		book_reader = csv.reader(csvfile)
		for row in book_reader:
			book_name = row[1]
			book_author = row[2]
			shelf_index = 18 #find_exclusive_shelf_field_index(row)
			if(row[shelf_index] == 'to-read'):
				wonderfulsite1_request = 'https://kat.cr/usearch/' + book_name + ' category:books/'
				wonderfulsite1_request = wonderfulsite1_request.replace(' ', '%20') 
				file_search_list.append(wonderfulsite1_request)
	for req in file_search_list: 
		found_success_pattern = 'http://torcache.net/torrent/1B9A4443D59CDA700103070B1B4C476D7806CFFC.torrent?title=[kat.cr]think.like.a.freak.by.steven.levitt.stephen.dubner.pdf'
		print(req)

if  __name__ =='__main__':
	main()