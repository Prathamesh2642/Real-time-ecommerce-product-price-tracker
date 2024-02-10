import undetected_chromedriver as webdriver
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
from time import sleep
from bs4 import BeautifulSoup
import re
import requests

browser = webdriver.Chrome(options=chrome_options)
browser.get('https://www.flipkart.com')
sleep(3)

# input_search = browser.find_element(By.ID, 'twotabsearchtextbox')
input_search_flipkart = browser.find_element(By.XPATH, "//input[@class='Pke_EE']")
search_button_flipkart = browser.find_element(By.XPATH, "//button[@type='submit']")

input_search_flipkart.send_keys("casio watches")
sleep(1)
search_button_flipkart.click()

products_flipkart = []
products_price_flipkart=[]
href_value=""

for i in range(2):
    if href_value=="":
            print('Scraping page', i+1)
            content=browser.page_source
            soup=BeautifulSoup(content,features="lxml")
            products_flipkart_all=soup.findAll('a',class_='IRpwTa')
            products_price_flipkart_all=soup.findAll('div',class_='_30jeq3')


            for prod in products_flipkart_all:
                products_flipkart.append(prod['title'])


            for price in products_price_flipkart_all:
                products_price_flipkart.append(price.text)
    
            next_button = soup.find('a', '_1LKTO3')
            href_value = next_button["href"]
            print(href_value)
            pattern = r'page=(\d+)'
            page_num=int(re.findall(pattern, href_value)[0])+1
            href_value = re.sub(pattern, "page="+str(page_num), href_value)            
            print(href_value)
    else:
            print('Scraping page', i+1)
            print('https://www.flipkart.com'+'/search?q=casio+watches&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=3')
            content=requests.get("https://www.flipkart.com"+href_value)
            soup=BeautifulSoup(content,"html.parser")
            products_flipkart_all=soup.findAll('a',class_='IRpwTa')
            products_price_flipkart_all=soup.findAll('div',class_='_30jeq3')


            for prod in products_flipkart_all:
                products_flipkart.append(prod['title'])


            for price in products_price_flipkart_all:
                products_price_flipkart.append(price.text)
    
            next_button = soup.find('a', '_1LKTO3')
            href_value = next_button["href"]
            print(href_value)
            pattern = r'page=(\d+)'


    # print(href_value+(str(int(re.findall(pattern, href_value)[0]))+1))

for i,j in zip(products_price_flipkart,products_flipkart):
    print(j,i)



browser.quit()