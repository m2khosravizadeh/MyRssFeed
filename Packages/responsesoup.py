'''
Rss-feed : Summery of the site what you want; news sites, Scientific Sites, Advertisement sites , etc.

*************
The main page
*************
My Resume & Characteristic: 

http://www.hamikar.com/fa/guest/cvlist/cv/96555/%D9%85%D8%AD%D9%85%D8%AF_%D8%AE%D8%B3%D8%B1%D9%88%DB%8C_%D8%B2%D8%A7%D8%AF%D9%87/

https://www.linkedin.com/in/mohammad-khosravizadeh-1943a96b

'''

from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError, MissingSchema, HTTPError
import requests


def soupresponse(vor):
    try:
        html_voroodi = requests.get(vor).content
        return BeautifulSoup(html_voroodi,'lxml')
    except MissingSchema or ConnectionError or HTTPError as e:
        return "big_bug_soup"
    
    


def isolation(parts , goal):
    tags = parts.find_all(goal) 
    return tags
