from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome('/home/owais/Downloads/chromedriver')

products = [] #list to store name of products
prices = [] #list to store name of products
ratings = [] #list to store name of products
driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq")
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
print(soup.prettify())
# soup = beautifulsoup4(content)
# for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
#     name = a.find('div', attrs={'class':'_3wU53n'})
#     price = a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
#     rating = a.find('div', attrs={'class':'hGSR34 _2beYZw'})
#     products.append(name.text)
#     prices.append(price.text)
#     ratings.append(rating.text) 
