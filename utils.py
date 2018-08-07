# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 22:52:41 2018

@author: USER
"""

import sys
from bs4 import BeautifulSoup as soup
import requests

def find_songs(song_name, p):
    song_path = '+'.join(song_name.lower().split(' '))
    page = requests.get('https://search.azlyrics.com/search.php?q={}&w=songs&p={}'.format(song_path,p))
    parsed = soup(page.content, 'html.parser')
    songs = parsed.find_all(class_ = 'text-left visitedlyr')

    if songs == []:
        return [], []
    else:
        b_tag_list = [song.find_all('b') for song in songs]
        song_list = [' / '.join(tag_content.get_text() for tag_content in b_tag) for b_tag in b_tag_list]
        song_urls = [song.find('a', href = True)['href'] for song in songs]
        
        return song_list, song_urls
    
def find_lyrics(lyrics_url):
    lyrics_page = requests.get(lyrics_url)
    parsed_lyrics_page = soup(lyrics_page.content, 'html.parser')
    lyrics = parsed_lyrics_page.find_all('div', class_ = None)[1].get_text().strip()
    return lyrics