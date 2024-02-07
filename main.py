import undetected_chromedriver as webdriver
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
from time import sleep
from bs4 import BeautifulSoup

# my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--use_subprocess")
# options = webdriver.ChromeOptions()
# options.add_argument(f"user-agent={my_user_agent}")


browser = webdriver.Chrome(options=chrome_options)
browser.get('https://www.amazon.in')
sleep(3)

input_search = browser.find_element(By.ID, 'twotabsearchtextbox')
search_button = browser.find_element(By.XPATH, "(//input[@type='submit'])[1]")

input_search.send_keys("casio watches")
sleep(1)
search_button.click()

products_amazon = []
products_price_amazon=[]
for i in range(2):
    print('Scraping page', i+1)
    product = browser.find_elements(By.XPATH, "//span[@class='a-size-base-plus a-color-base a-text-normal']")
    product_price = browser.find_elements(By.XPATH, "//span[@class='a-price-whole']")
    for p,j in zip(product,product_price):
        products_amazon.append(p.text)
        products_price_amazon.append(j.text)
    # print(products)
    # print(products_price)
    next_button = browser.find_element(By.XPATH, "//a[text()='Next']")
    next_button.click()
    sleep(4)


print(len(products_amazon),len(products_price_amazon))

del products_price_amazon[:3]
print(len(products_amazon),len(products_price_amazon))
dict={}
for i in range(len(products_price_amazon)):
    print(i,products_amazon[i],products_price_amazon[i],)
    dict[products_amazon[i]]=products_price_amazon[i]





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
for i in range(2):
    print('Scraping page', i+1)
    content=browser.page_source
    soup=BeautifulSoup(content,features="lxml")
    products_flipkart_all=soup.find_all('a',class_='IRpwTa')
    products_price_flipkart_all=soup.find_all('a',class_='_30jeq3')
    print(products_price_flipkart_all)
    # for p,j in zip(products_flipkart_all,products_price_flipkart_all):

    #     products_flipkart.append(p['title'])


        # print(p['title'])
        # products_price_flipkart.append(j['text'])
    # print(products_flipkart)
    # print(products_price_flipkart)
    # products_flipkart = browser.find_elements(By.XPATH, "//a[@class='IRpwTa']")
    # products_flipkart=browser.find_elements( By.CLASS_NAME, 'IRpwTa' )
    # products_price_flipkart = browser.find_elements(By.XPATH, "//div[@class='_30jeq3']")
    # print(products_flipkart)
    # for p,j in zip(products_flipkart,products_price_flipkart)):
    #     print(p[0])
    #     # products_flipkart.append(p.title)
    #     products_price_flipkart.append(j.title)
    # print(products)
    # print(products_price)
    # next_button = browser.find_element(By.XPATH, "//a[@class='_1LKTO3']")
    # href_value = next_button.get_attribute("href")
    # print(href_value)
    # elems = WebDriverWait(webdriver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".sc-eYdvao.kvdWiq [href]")))        
    # next_button['href'].click()
    # sleep(4)



# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Example with WebDriverWait
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "captchacharacters"))
#     )
#     # Now you can interact with the element
# except NoSuchElementException:
#     print("Element not found")
