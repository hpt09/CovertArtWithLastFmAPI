# -*- coding: utf-8 -*-
"""
Created on Mon May 27 15:40:04 2019

@author: hpt09
"""

import csv
import pylast
import urllib.request

API_KEY = "44a1374b21dd3bb74687daaa49834971"  
API_SECRET = "b09d4d043aeb495cbcbe9959257c139c"

# In order to perform a write operation you need to authenticate yourself
username = "hpt09"
password_hash = pylast.md5("Dr@gon12")

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)

filename = 'output.csv'

with open(filename, 'r',  encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    data = [row for row in csv_reader]
    line = data[0]
    artist_name = line[0]
    title = line[1]
    track = network.get_track(artist_name, title)
    try:
        url = track.get_cover_image()
    except:
        print("not found")
    
    #print(url)
    
    
# =============================================================================
#     for line in csv_reader:
#         print(line[1:2])
# =============================================================================
        
def download_web_image(url, name):
    full_name = name + ".png"
    urllib.request.urlretrieve(url, full_name)