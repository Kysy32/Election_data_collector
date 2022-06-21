"""
colector.py: Third project to Engeto Online Python Academy
author: Jakub Kyselý
email: jkysely@centrum.cz
discord: Kysy#6104
"""

import os
import sys
import csv


from requests import get
from bs4 import BeautifulSoup

def user_inputs():
    '''
    Control if user inputs are correct.
    :return: link, file_name
    '''

    if len(sys.argv) != 3:
        print(
            "Missing arguments to run:  'script name', 'link' or 'file name (.csv)",
            "Entry: python colector.py 'link', 'file_name.csv'",
            sep="\n")
        quit()

    elif "https://volby.cz/pls/ps2017nss/" not in sys.argv[1]:
            print("Please insert link on election result on first position (from portal volby.cz")
            quit()

    else:
        if sys.argv[2].endswith('.csv'): # control if user use csv file
            link = sys.argv[1]
            file_name = sys.argv[2]

            return link, file_name

        else:
            print('You must insert "file_name.csv"')
            quit()

def html_to_str(link):
    '''
    Take a html code and transform it to the string
    :param link:
    '''

    html = get(link) #take html from web
    string = html.text #transform html to string

    return string

def soup(string_html):
    '''
    Transform html_string to soup object
    :param string_html:
    '''

    split_html = BeautifulSoup(string_html, 'html.parser')

    return split_html


def colector():
    '''
    Webscraping the web and save the data (election) like csv file.
    '''

    link, file_name = user_inputs()
    string_html = html_to_str(link)
    split_html = soup(string_html)
    print(split_html)

colector()