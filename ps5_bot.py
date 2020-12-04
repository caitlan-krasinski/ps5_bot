from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from twilio.rest import Client

#enter path to your chrome driver
driver = webdriver.Chrome('**************')

#open PS5 link for best buy
driver.get('https://www.bestbuy.ca/en-ca/product/playstation-5-console-online-only/14962185')

#twilio account info
#enter your personal SID and AUTH Token 
client = Client("*************", "**************")

#refresh as long as add to cart is disabled 
while not driver.find_element_by_xpath('//*[@id="test"]/button').is_enabled():
    driver.refresh()
    time.sleep(1)
    y = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="test"]/button')))
    print('refresh')

#click add to cart
y = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="test"]/button')))
driver.find_element_by_xpath('//*[@id="test"]/button').click()

#click to view your cart 
y = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="cartIcon"]/div[2]/div/div/div/section/div/button')))
driver.find_element_by_xpath('//*[@id="cartIcon"]/div[2]/div/div/div/section/div/button').click()

#click to proceed to checkout
y = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/div[4]/div[2]/div[2]/section/div/section/section[2]/div[2]/div/a')))
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[4]/div[2]/div[2]/section/div/section/section[2]/div[2]/div/a').click()


#send text msg notifying that item in in cart
#Add your twilio phone number and personal number into to and from 
client.messages.create(to="*********", 
                       from_="********", 
                       body="PS5 is in your cart!")

#click to proceed to checkout as a guest
driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div/div/div[2]/div/div[2]/a').click()
