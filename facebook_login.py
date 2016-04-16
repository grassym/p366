#!/usr/bin/python
# -*- coding: utf-8 -*-

import facebook
import requests

file = open("/home/olia/Documents/fuck_the_code/facebook_credentials.txt") 

app_id = file.readline()
app_secret = file.readline()
graph_api_token = file.readline()

# print ("app_id = " + str(app_id))
# print ("app_secret = " + str(app_secret))

# def get_fb_token(app_id, app_secret):           
#     payload = {'grant_type': 'client_credentials', 'client_id': app_id, 'client_secret': app_secret}
#     file = requests.post('https://graph.facebook.com/oauth/access_token?', params = payload)
#     # print file.text #to test what the FB api responded with    
#     result = file.text.split("=")[1]
#     print result #to test the TOKEN
#     return result

# token = get_fb_token(app_id, app_secret)

graph = facebook.GraphAPI(graph_api_token)

tt = graph.get_object("me")
#print tt#['friends']

friends = graph.get_connections("me", "friends")['data']
print friends