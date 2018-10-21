# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 11:41:10 2016

@author: Chris Loewenthal, Alex Littaua, Garrett Webb, Ethan Bonavida
"""

from configparser import ConfigParser
import requests
import json

#Add your own subscription key and customConfigId through a separate config.cfg
cp = ConfigParser()
cp.read('config.cfg')
sKey = cp.get('auth', 'subscriptionKey')
ccid = cp.get('auth', 'customConfigId')

#Ask the user for a search query
searchTerm = input("Enter your search query: ")

#Passes the query to the custom search interface and returns the results in a JSON request
url = 'https://api.microsoft.com/bingcustomsearch/v7.0/search?q=' + searchTerm + '&customconfig=' + ccid
r = requests.get(url, headers={'Ocp-Apim-Subscription-Key': sKey})
print(r)
