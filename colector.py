"""
colector.py: Third project to Engeto Online Python Academy
author: Jakub Kyselý
email: jkysely@centrum.cz
discord: Kysy#6104
"""

import sys
import csv


from requests import get
from bs4 import BeautifulSoup

def user_inputs():
    '''
    Control if user inputs are correct.
    :return: link, file_name
    '''

    if len(sys.argv) != 3: # control if user used all arguments
        print(
            "Missing arguments to run:  'script name', 'link' or 'file name (.csv)",
            "Entry: python colector.py 'link', 'file_name.csv'",
            sep="\n")
        quit()

    elif "https://volby.cz/pls/ps2017nss/" not in sys.argv[1]: # control if user used a correct link
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

    html = get(link) # take html from web
    string_html = html.text # transform html to string

    return string_html

def soup(string_html):
    '''
    Transform html_string to soup object
    :param string_html:
    '''

    split_html = BeautifulSoup(string_html, 'html.parser')

    return split_html

def td_tags(split_html):
    '''
    Create link with open page with data for all municipalities
    :param split_html:  
    '''

    tags = split_html.find_all("td", {"class": "cislo"})

    links = []
    for tag in tags:
        x = tag.a['href']
        link = f'https://volby.cz/pls/ps2017nss/{x}'
        links.append(link)

    return links

def find_electoral_parties(links):
    '''
    Finds all electoral parties in the monitored region
    :param link:
    '''
    parties_list = [] # empty list for parties in monitored region

    html_str = get(links[0])
    soup = BeautifulSoup(html_str.content, 'html.parser')
    parties = soup.find_all(class_="overflow_name")

    for party in parties:
        parties_list.append(party.getText()) # get a party name and append it to the list


def colector():
    '''
    Webscraping the web and save the data like csv file.
    '''

    link, file_name = user_inputs()
    string_html = html_to_str(link)
    split_html = soup(string_html)
    links = td_tags(split_html)
    parties = find_electoral_parties(links)
    print(parties)



# run the web scraping
colector()
