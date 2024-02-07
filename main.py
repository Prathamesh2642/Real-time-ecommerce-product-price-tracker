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