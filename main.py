import undetected_chromedriver as webdriver
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
from time import sleep
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--use_subprocess")

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
