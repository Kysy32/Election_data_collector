"""
collector.py: Third project to Engeto Online Python Academy
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
    Controls if user inputs are correct.
    :return: link, file_name
    '''

    if len(sys.argv) != 3: # control if user used all arguments
        print(
            "Missing arguments to run:  'script name', 'link' or 'file name (.csv)",
            "Entry: python collector.py 'link', 'file_name.csv'",
            sep="\n")
        quit()

    elif not sys.argv[1].startswith('https://volby.cz/pls/ps2017nss/'): # control if user used a correct link
        print("Please insert link on election result on first position (from portal volby.cz)")
        quit()

    elif not sys.argv[2].endswith('.csv'): # control if user use csv file
        print('You must insert "file_name.csv"')
        quit()

    else:
        link = sys.argv[1]
        file_name = sys.argv[2]

        return link, file_name

def html_to_str(link):
    '''
    Takes a html code and transform it to the string
    :param link:
    '''

    html = get(link) # take html from web
    string_html = html.text # transform html to string

    return string_html


def soup(string_html):
    '''
    Transforms html_string to soup object
    :param string_html:
    '''

    split_html = BeautifulSoup(string_html, 'html.parser')

    return split_html

def td_tags(split_html):
    '''
    Creates link witch open page with data for all municipalities
    :param split_html:  
    '''

    tags = split_html.find_all("td", {"class": "cislo"})

    links = [] # empty list for links
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

    return parties_list

def create_header(parties):
    '''
    Creates header for csv file
    :param parties:
    '''

    header = ["Kód obce", "Název obce", "Voliči v seznamu", "Vydané obálky", "Platné hlasy"]

    header.extend(parties)

    return header

def create_names_list(link):
    '''
    Creates a list of municipalities names
    :param link:
    '''
    name_list = []

    html_str = get(link)
    soup = BeautifulSoup(html_str.content, 'html.parser')
    names = soup.find_all(class_="overflow_name")

    for name in names:
        name_list.append(name.getText()) # get a village name and append it to the list

    return name_list

def create_codes_list(link):
    '''
    Creates a list of municipalities codes
    :param link:
    '''
    code_list = []

    html_str = get(link)
    soup = BeautifulSoup(html_str.content, 'html.parser')
    codes = soup.find_all(class_="cislo")

    for code in codes:
        code_list.append(code.getText()) # get a village code and append it to the list

    return code_list

def create_votes_statistic_list(links):
    '''
    Find a save election data (number of voters, issued envelopes, valid votes)
    :param links:
    '''

    votes_info = []

    for link in links:
        list = []

        html_str = get(link)
        soup = BeautifulSoup(html_str.text, 'html.parser')

        voter = soup.find("td", {"headers": "sa2"}).text
        envelopes = soup.find("td", {"headers": "sa3"}).text
        valid_votes = soup.find("td", {"headers": "sa6"}).text

        list.append(voter.replace("\xa0", ""))
        list.append(envelopes.replace("\xa0", ""))
        list.append(valid_votes.replace("\xa0", ""))

        votes_info.append(list)

    return votes_info

def create_parties_votes_list(links):
    '''
    Find a save election data (number of voters, issued envelopes, valid votes)
    :param links:
    '''

    parties_votes_fin = []

    for link in links:

        html_str = get(link)

        parties_votes = []

        soup = BeautifulSoup(html_str.content, 'html.parser')
        parties_first_part = soup.find_all(headers="t1sa2 t1sb3")

        for party in parties_first_part:
            parties_votes.append(party.getText().replace("\xa0", ""))

        parties_second_part = soup.find_all(headers="t2sa2 t2sb3")

        for party in parties_second_part:
            parties_votes.append(party.getText().replace("\xa0", ""))

        parties_votes_fin.append(parties_votes)

    return parties_votes_fin

def save_data_to_one_list(code_list, name_list, vote_statistic_list, parties_statistic_list):
    '''
    Save all selected data to one list
    :param code_list:
    :param name_list:
    :param vote_statistic_list:
    :param parties_statistic_list:
    '''

    data_list = [] # empty list for final dataset

    # joins lists using indexes
    for x in range(0,len(name_list)):
        temp = []

        temp.append(code_list[x])
        temp.append(name_list[x])
        temp.extend(vote_statistic_list[x])
        temp.extend(parties_statistic_list[x])

        data_list.append(temp) # create list with all data for one municipality

    return data_list

def write_data_to_csv(file_name,header, final_dataset):
    '''
    Crate csv file with selected data
    :param final_dataset:
    :return:
    '''

    # write the data to csv file
    with open(file_name, mode='w', encoding='utf-8', newline='') as new_csv:
        writer = csv.writer(new_csv)
        writer.writerow(header)
        writer.writerows(final_dataset)


def colector():
    '''
    Searching the web and save the data like csv file.
    '''

    # Proces function
    link, file_name = user_inputs()
    string_html = html_to_str(link)
    split_html = soup(string_html)
    links = td_tags(split_html)

    print(f'DOWNLOADING DATA FROM URL: {link}')

    # Create header for csv file
    parties = find_electoral_parties(links) # list with parties in region
    header = create_header(parties) # prepare header for csv file

    # Find and save selected data
    name_list = create_names_list(link) # list with municipalities names
    code_list = create_codes_list(link) # list with municipalities codes
    vote_statistic_list = create_votes_statistic_list(links) # list with selected statistic (number of voters, issued envelopes, valid votes)
    parties_statistic_list = create_parties_votes_list(links) # list with votes for every party in region

    # Save all selected data to one list
    final_dataset = save_data_to_one_list(code_list,name_list,vote_statistic_list,parties_statistic_list)

    print(f'SAVING DATA TO FILE: {file_name}')

    # Create csv file with selected data
    write_data_to_csv(file_name,header,final_dataset)

    print('TERMINATING colector.py, ALL DATA ARE SAVED. ')

# run the web scraping
if __name__ == "__main__":
    colector()