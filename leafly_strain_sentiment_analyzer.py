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

    #now we bring in the webdriver, NOTE: I am using the version 80.blah driver because i have version 80 on chrome, if you get an error 
    # on this next line it is probably because you have the wrong chromedriver for your chrome version. you can find your chrome version in the settings menu, and download a new driver from https://chromedriver.chromium.org/downloads
    driver = webdriver.Chrome('./Chrome/chromedriver')

    #setting up a small (maybe not so small at the end) list for holding strain pages (these pages are going to be the views for a list of strains, 
    # not the individual strain-pages, sorry if the wording is confusing here). to cut down on a little bit of space I am also adding a prefix that will be used later
    site_prefix = "leafly.com"
    list_of_strain_pages = []
    #this is where some research kicks in from last night (25th) - I know that the pages all follow the pattern: 'leafly.com/strains?sort=name&page=X


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
