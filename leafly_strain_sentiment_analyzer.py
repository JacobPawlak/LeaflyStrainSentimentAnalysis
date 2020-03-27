#Jacob Pawlak
#leafly_strain_sentiment_analyzer.py
#march 26th, 2020
#goooo blue team!

#################### IMPORTS ####################
#pulling in json and pandas as always for file output (json and csv)
import json
import pandas

#going to do senti stuff so i need nltk and our fun tools in there
import nltk
from nltk import tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import emoji

#now to import all of our webscraping tools (bs4 and selenium)
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#now for the other system libraries and extra bits
import re
import os
import sys
import time


#################### HELPERS ####################

#just going to throw this open file helper function in here since I use it in almost every other program i write
def open_file(file_path):
    #since i will probably reuse this helper i am going to make sure it can accept multiple file types
    #for pulling in csv into pandas dataframe
    if(file_path.split('.')[-1].lower() == 'csv'):
        dataframe = pandas.read_csv(file_path)
        print('returning a pandas dataframe')
        return dataframe
    #for pulling json files into [{}] structures
    elif(file_path.split('.')[-1].lower() == 'json'):
        data_file = open(file_path, 'r')
        data_list = []
        for line in data_file:
            data_list = eval(line)
        print('returning a list of dictionaries')
        return data_list
    #basically same thing as the json file, just saved as a text file
    elif(file_path.split('.')[-1].lower() == 'txt'):
        data_file = open(file_path, 'r')
        data_list = []
        for line in data_file:
            data_list = eval(line)
        print('returning a list of dictionaries')
        return data_list
    #if the filetype doesnt match on of our cases, just return
    else:
        print("You passed in an unrecognized file type, please use a csv, json, or txt file")
        return None

#this helper function will be used to grab the strain names, strain pages, etc lists from leafly. it should return at least one list of strain pages
def scrape_list_of_strains():

    #since this is more of a bespoke project and not really intended to be agnostic, i dont see a big point in trying to load a bunch of
    # datafiles in here, so yes i am going to _hard code_ some links and stuff in this helper

    #like always, gotta make a save file when doing stuff over network (you know the drill by now if youre reading this)
    savefile = open('list_of_strain_pages.txt', 'w')

    '''
    #setting up a small (maybe not so small at the end) list for holding strain pages (these pages are going to be the views for a list of strains, 
    # not the individual strain-pages, sorry if the wording is confusing here). to cut down on a little bit of space I am also adding a prefix that will be used later
    site_prefix = "https://leafly.com"
    list_of_strain_pages = []
    #this is where some research kicks in from last night (25th) - I know that the pages all follow the pattern: 'leafly.com/strains?sort=name&page=X' when sorting by name (the only way to get consitant results)
    # it looks like it will lend itself to an easy list comprehension:
    [list_of_strain_pages.append('/strains?sort=name&page={}'.format(page_num)) for page_num in range(1, 115)]
    
    #here is where we gotta add a few counters and extras, we'll fill this out as needed
    strain_counter = 0
    list_of_strain_names = []
    '''

    #okay so after some testing it turns out that the webdriver wont let me do the sort by name thing so im just going to have to start on a page and click the next button over and over
    #setting up some new prefixes and stuff
    site_prefix = "https://leafly.com/strains"
    list_of_strain_names = []
    strain_counter = 0

    #now we bring in the webdriver, NOTE: I am using the version 80.blah driver because i have version 80 on chrome, if you get an error 
    # on this next line it is probably because you have the wrong chromedriver for your chrome version. you can find your chrome version in the settings menu, and download a new driver from https://chromedriver.chromium.org/downloads
    print("It is my experience that you will need to click the \"I am over 21\" button in the popup before you can proceed to the site. Sleeping for 10 seconds after you see this.")
    driver = webdriver.Chrome('./Chrome/chromedriver')
    driver.get(site_prefix)
    time.sleep(10)
    #now to grab the page source and pull the strain links out of it. we can use the find_all to look for the <a> tags and then pull the href out of them
    # we can also take this time to write out to our savefile
    soup = BeautifulSoup(driver.page_source, 'html5lib')
    strain_links = soup.find_all('a', attrs={'class': 'strain-tile'})
    [list_of_strain_names.append(strain['href']) for strain in strain_links]
    [savefile.write("{}\n".format(str(strain['href']))) for strain in strain_links]
    
    #we can move on to the next page since we are done
    next_btn = driver.find_element_by_link_text("Next")
    next_btn.click()

    #now to lazily loop through all of the rest of the pages, then we can do the same thing as above
    curr_page_number = driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div[4]/span').text.split()
    #the curr_page_number should look like the '1 of 114' text at the bottom of the page. i am interested in the two numbers

    while(int(curr_page_number[0]) < int(curr_page_number[2])):
        #like i said, we just have to do it all again
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, 'html5lib')
        strain_links = soup.find_all('a', attrs={'class': 'strain-tile'})
        [list_of_strain_names.append(strain['href']) for strain in strain_links]
        [savefile.write("{}\n".format(str(strain['href']))) for strain in strain_links]
        next_btn = driver.find_element_by_link_text("Next")
        next_btn.click()

    return

def add_senti_analysis(review_obj):

    return

#todo: use streamlit maybe (or just export it and figure out how to use powerbi/tableu(sp) i guess)
def build_dashboard():
    return

#################### MAIN () ####################

def main():

    print()

main()
