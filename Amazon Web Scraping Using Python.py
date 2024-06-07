#!/usr/bin/env python
# coding: utf-8

# In[18]:


from bs4 import BeautifulSoup
import requests
import time
import datetime

###
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

####
import smtplib


# In[44]:


# connect to website

URL ="""
https://www.amazon.com/funny-analyst-definition-scientist-t-shirt/dp/B07NLP2PKY/ref=sr_1_6?crid=QZ0NZSX2RS7P&dib=eyJ2IjoiMSJ9.PM2zhQFx_lfPnddZwr05DlG0nE9SZQplkaSox68h2gWi7NZa8Tx1lP3jupAKZ_m9_aO5BkVAzxX8SkggOgtsvIYdFQSNZE04wyffLxVPelO4JjB3iY-oZK4jKD6bm5oU6TYIssSx0TOB9n9adUdctWfrSWBY872M4s6qdhZURtfhxkkc-a_pfktGCvBF4rBcSlWKPhp0_ULM0v4LdGaI56cIq7Ml1pi2SLlRIvXecY4-RZxC5Rd2SQCyda_6YFdrGZIPxocHmiP9ZtT3u1st0zYW7_I6sQ2ykXqQgbw55Ts.BAOAqpex0VXqvPNZlATtDPe64pB4loEMK7VGxg0FvRQ&dib_tag=se&keywords=data+analyst+tshirt&qid=1717533241&sprefix=data+analyst+tshirt%2Caps%2C405&sr=8-6
"""

headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36" }
    
page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "lxml")

#soup1 
soup2 = BeautifulSoup(soup1.prettify(), "lxml")
#soup2

price_symbol = soup2.find(class_='a-price-symbol').get_text(strip=True)
price_whole = soup2.find(class_='a-price-whole').get_text(strip=True)
price_fraction = soup2.find(class_='a-price-fraction').get_text(strip=True)
price = f'{price_symbol}{price_whole}{price_fraction}'
price
#productTitle
#title = soup2.find(id='productTitle').get_text()

#print(title)
#price = soup2.find(id='aok-offscreen').get_text()
#soup2.find('span', class_='aok-offscreen').get_text(strip=True)


#print(title)
#print(price)





# In[69]:


URL ="""
https://www.amazon.com/funny-analyst-definition-scientist-t-shirt/dp/B07NLP2PKY/ref=sr_1_6?crid=QZ0NZSX2RS7P&dib=eyJ2IjoiMSJ9.PM2zhQFx_lfPnddZwr05DlG0nE9SZQplkaSox68h2gWi7NZa8Tx1lP3jupAKZ_m9_aO5BkVAzxX8SkggOgtsvIYdFQSNZE04wyffLxVPelO4JjB3iY-oZK4jKD6bm5oU6TYIssSx0TOB9n9adUdctWfrSWBY872M4s6qdhZURtfhxkkc-a_pfktGCvBF4rBcSlWKPhp0_ULM0v4LdGaI56cIq7Ml1pi2SLlRIvXecY4-RZxC5Rd2SQCyda_6YFdrGZIPxocHmiP9ZtT3u1st0zYW7_I6sQ2ykXqQgbw55Ts.BAOAqpex0VXqvPNZlATtDPe64pB4loEMK7VGxg0FvRQ&dib_tag=se&keywords=data+analyst+tshirt&qid=1717533241&sprefix=data+analyst+tshirt%2Caps%2C405&sr=8-6
"""

headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36" }
    
page = requests.get(URL)

soup1 = BeautifulSoup(page.content, "lxml")
soup2 = BeautifulSoup(soup1.prettify(), "lxml")


price_symbol = soup2.find(class_='a-price-symbol').get_text(strip=True)
price_whole = soup2.find(class_='a-price-whole').get_text(strip=True)
price_fraction = soup2.find(class_='a-price-fraction').get_text(strip=True)
price = f'{price_symbol}{price_whole}{price_fraction}'



print(price)


# In[ ]:





# In[ ]:




