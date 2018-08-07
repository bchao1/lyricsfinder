# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 18:53:18 2018

@author: USER
"""

import tkinter as tk
from tkinter.ttk import Separator, Style
import utils

class GUI:
    def __init__(self, root, imsrc):
        self.root = root
        self.logo = imsrc
        
        self.curr_page = None
        self.user_query = ''
        self.song_urls = []
        self.song_list = []
        
        self.config_All()
        
        
    def config_All(self):
        
        self.config_root()
        self.config_Label()
        self.config_Entry()
        self.config_Text()
        self.config_Button()
        self.config_Style()
        
    def config_root(self):
        root.title('  Lyrics Finder')
        root.iconbitmap('./src/icon.ico')
        #root.configure(background = 'white')
        root.columnconfigure(0,
                             weight = 1, 
                             uniform = 'half')
        
        root.columnconfigure(1,
                             weight = 1, 
                             uniform = 'half')
    def config_Label(self):
        
        welcome_text = ('Welcome to Lyrics Finder,\n'
                        'you can search for lyrics by\n'
                        'typing in the name of the song')
    

        
        tk.Label(root, 
                 text = welcome_text,
                 justify = tk.LEFT).grid(row = 0,
                                  column = 0,
                                  columnspan = 2,
                                  sticky = 'w',
                                  padx = 10)
        
        tk.Label(root, 
                 image = self.logo).grid(row = 0,
                           column = 2,
                           columnspan = 5,
                           sticky = 'eswn')
        
        tk.Label(root,
                 text='Enter song name: ',
                 justify = tk.LEFT).grid(row = 1, 
                                  column = 0, 
                                  columnspan = 2,
                                  sticky = 'w',
                                  padx = 10)
        
        self.search_result_label = tk.Label(root,
                                            text = 'Search Results')
        self.search_result_label.grid(row = 2,
                                      column = 0,
                                      columnspan = 2)
        
        self.title_artist_label = tk.Label(root,
                                           text = 'Title / Artist')
        self.title_artist_label.grid(row = 3, 
                                     column = 2, 
                                     columnspan = 5)
        
        tk.Label(root,
                 text = 'Song# ').grid(row = 3,
                                column = 0,
                                sticky = 'eswn')
        
        
    def config_Entry(self):
        self.song_search_entry = tk.Entry(root)
        self.song_search_entry.grid(row = 1,
                              column = 2,
                              columnspan = 4,
                              sticky = 'eswn')
        
        self.song_num_enter = tk.Entry(root)
        self.song_num_enter.grid(row = 3,
                                 column = 1,
                                 sticky = 'eswn')
        
    def config_Text(self):
        self.search_results = tk.Text(root, width = 50)
        self.search_results.grid(row = 4,
                                 column = 0,
                                 columnspan = 2)
    
        self.lyrics_content = tk.Text(root,width = 55)
        self.lyrics_content.grid(row = 4,
                                 column = 2,
                                 columnspan = 4)
        
        self.scroll = tk.Scrollbar(root)
        self.scroll.grid(row = 4,
                         column = 6,
                         sticky = 'eswn')

        self.scroll.config(command = self.lyrics_content.yview)
        self.lyrics_content.config(yscrollcommand = self.scroll.set)
        
        
    def config_Style(self):
        Separator(root, 
                  orient = 'horizontal').grid(row = 1,
                                       column = 0,
                                       columnspan = 7,
                                       sticky = 'esw')
        Separator(root, 
                  orient = 'horizontal').grid(row = 0,
                                       column = 0,
                                       columnspan = 7,
                                       sticky = 'esw')
    def config_Button(self):
        tk.Button(root,
                  text = 'Previous',
                  command = self.prev_page_callback).grid(row = 5,
                                              column = 0,
                                              sticky = 'eswn')

        tk.Button(root,
                  text = 'Next',
                  command = self.next_page_callback).grid(row = 5,
                                                   column = 1,
                                                   sticky = 'eswn')
        
        tk.Button(root, 
                  text = 'Submit',
                  command = self.first_query).grid(row = 1,
                                            column = 6,
                                            sticky = 'eswn')
        tk.Button(root,
                  text = 'Show lyrics',
                  command = self.show_lyrics).grid(row = 2,
                                            column = 2,
                                            columnspan = 5,
                                            sticky = 'eswn')
        tk.Button(root,
                  text = 'Download',
                  command = self.download).grid(row = 5,
                                         column = 2,
                                         columnspan = 5,
                                         sticky = 'eswn')

    def first_query(self):
        self.user_query = self.song_search_entry.get()
        if self.user_query == '':
            return
        
        self.curr_page = 1
        self.lyrics_content.delete(1.0, tk.END)
        self.title_artist_label.config(text='Title / Artist')
        self.surf_pages()
        
    def prev_page_callback(self):
        if self.user_query == '':
            return
    
        if self.curr_page > 1:
            self.curr_page -= 1
        self.surf_pages()
        
    def next_page_callback(self):
        if self.user_query == '':
            return
        
        self.curr_page += 1
        self.surf_pages()
        
    def surf_pages(self):
        self.song_list, self.song_urls = utils.find_songs(self.user_query,
                                                          self.curr_page)
            
        if self.song_list == []: # Unsuccessful query, no matching songs found
            self.search_results.delete(1.0, tk.END)
            self.search_results.insert(tk.END, 
                                       'No results match for \'{}\''.
                                       format(self.user_query))
        else:
            result = '\n'
            for i in range(len(self.song_list)):
                result += ('{:3}. {}'.format(i+1, self.song_list[i]) + '\n')
            self.search_results.delete(1.0, tk.END)
            self.search_results.insert(tk.END, result)
            
            
            self.search_result_label.config(text = 'Search Results for \'{}\', page {}'.
                                            format(self.user_query, self.curr_page))
            
    def show_lyrics(self):
        song_num = self.song_num_enter.get()
        
        if song_num == '': # No input
            return
        if not song_num.isnumeric(): # Invalid input, not numerical index
            return
        
        song_num = int(song_num) # Cast user input to integer type
         
        if self.song_list != []: # Query is successful
            if 0 < song_num <= len(self.song_list): # Song number within range
                lyrics_url = self.song_urls[song_num - 1]
                song_name = self.song_list[song_num - 1]
                self.title_artist_label.config(text = song_name)
                
                lyrics = utils.find_lyrics(lyrics_url)
                self.lyrics_content.delete(1.0, tk.END)
                self.lyrics_content.insert(tk.END, lyrics)
    
    def download(self):
        pass
        
    def run(self):
        self.root.mainloop()
        

if __name__ == '__main__':
    root = tk.Tk()
    
    img = tk.PhotoImage(file = './src/music.gif').subsample(2,2)

    lyricsfinderGUI = GUI(root, img)
    lyricsfinderGUI.run()