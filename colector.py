import os
import sys
import csv

from requests import request
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
            sep="\n"
        )
    else:
        if sys.argv[2].endswith('.csv'): # control if user use csv file
            link = sys.argv[1]
            file_name = sys.argv[2]

            return link, file_name
        else:
            print('You must insert "file_name.csv"')
            quit()

def colector():
    '''

    '''
    link, file_name = user_inputs()
    #print(link,file_name)

colector()