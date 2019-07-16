#!/usr/bin/env python
# coding: utf-8

# In[307]:


#Intructions to create the HTML file
#
#Go to pingboard
#
#Directory>Company Internal Departments
#
#Go to the bottom of the list and load all people. Right click on a picture and inspect
#
#Go to the HTML code, select the second line, <html>, right click>copy>copy outer HTML
#
#Paste to an HTML text file


# In[308]:


from urllib.request import urlopen
#from urllib2 import urlopen
from bs4 import BeautifulSoup
import smtplib, ssl
import requests
import csv


# In[309]:


#input name of the file
filename ='Insidesales.html'
outfile = 'Insidesales2.csv'

#open(filename, 'w').close()

file = open(filename, "r")


# In[310]:


soup = BeautifulSoup(file, 'html.parser')


# In[311]:


divTag = soup.findAll('div',{'class':'roster-card roster-card--user roster-card--clickable'})
#feels_box = soup.find('span', attrs={'class':'deg-feels'})


# In[312]:


len(divTag)


# In[313]:


#<div class="text--sm text--subtle break-word" title="Job title">Director of Sales</div>
#<div class="timestamp updated" title="2016-05-08T1231Z">May 8, 12:31 PM EDT</div>

file2=open(outfile, "w")

for tag in divTag:
    name = tag.find('div',{'class':'roster-card__title'}).text
    src= tag.find('img')['src']
    try:
        position = tag.find_all('div',{'class':'text--sm text--subtle break-word tooltipstered'})[0].text
    except:
        position = tag.find_all('div',{'class':'text--sm text--subtle break-word'})[0].text
        pass
    try:
        location = tag.find_all('div',{'class':'text--sm text--subtle break-word tooltipstered'})[1].text
    except:
        location = tag.find_all('div',{'class':'text--sm text--subtle break-word'})[1].text
        pass
    
    #position = tag.find_all('div',{'class':'text--sm text--subtle break-word tooltipstered'})
    #print(position)
    #location = tag.find('div',{'class':'text--sm text--subtle break-word tooltipstered'})['Office Location']
    
    print(name + position + location)
    file2.write(name + "; " + position + ";" + location + ";" + src +'\r')

