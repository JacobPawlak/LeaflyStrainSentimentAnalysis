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
