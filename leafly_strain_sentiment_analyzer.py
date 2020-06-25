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

    next_links = driver.find_elements_by_css_selector("a.flex.items-center.pl-sm")
    #print(next_links)
    #print(len(next_links))
    next_links[-1].click()

    time.sleep(3)

    for i in range(0, 113):
    #while(int(curr_page_number[0]) < int(curr_page_number[2])):
        #like i said, we just have to do it all again...
        #let the page load for a sec
        #grab the page source to parse through
        print("Scraping page {}".format(str(i+2)))
        soup = BeautifulSoup(driver.page_source, 'html5lib')
        #find all the strain tiles
        strain_links = soup.find_all('a', attrs={'class': 'strain-tile'})
        #add to the strain_names list 
        [list_of_strain_names.append(strain['href']) for strain in strain_links]
        #write out to our save file for safe keeping
        [savefile.write("{}\n".format(str(strain['href']))) for strain in strain_links]
        #find and click the next page button

        next_links = driver.find_elements_by_css_selector("a.flex.items-center.pl-sm")
        #print(next_links)
        #print(len(next_links))
        next_links[-1].click()

        time.sleep(3)

    print("Found {} of strains!".format(len(list_of_strain_names)))

    driver.quit()
    #now that we are done grabbing all of the names, it is time to start making our strain dicts and loading them up with data

    return list_of_strain_names

def collect_reviews(review_links):

    return

def add_senti_analysis(review_obj):

    return

#todo: use streamlit maybe (or just export it and figure out how to use powerbi i guess)
def build_dashboard():
    return

#################### MAIN () ####################

def main():

    print("Starting...")

    list_of_strain_names = scrape_list_of_strains()

    review_links = ["https://leafly.com{}/reviews".format(strain) for strain in list_of_strain_names]

    collect_reviews(review_links)

main()
