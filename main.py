import sys
import time
import requests
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# find the element with explicit wait
def GetTextValue(xpath):   
    element = WebDriverWait(driver,40).until(
    EC.presence_of_element_located((By.XPATH,xpath))
    )
    return element.text
def Click(xpath):
    element = WebDriverWait(driver,40).until(
    EC.presence_of_element_located((By.XPATH,xpath))
    )
    element.click()

def switchframe(xpath):
    element = WebDriverWait(driver,40).until(
    EC.presence_of_element_located((By.XPATH,xpath))
    )
    driver.switch_to.frame("abhimanyu")

def validateall(driver):
    element = driver.find_element_by_xpath('//*[@id="vrequest"]').text
    print(element)


#executable_path="C:/Users/c-nitesh.agarwal/Desktop/selenium/geckodriver"
driver = webdriver.Firefox(executable_path="/home/tanusha/Desktop/selenium/geckodriver")
driver.maximize_window()
driver.get("https://stats.slike.in/login")  
time.sleep(10)

# login
username = driver.find_element_by_xpath('//*[@id="email"]').send_keys("slikesuper")
password = driver.find_element_by_xpath('//*[@id="password"]').send_keys(" slik3!$uper@")
driver.find_element_by_xpath('//*[@id="submitBtn"]').click()
time.sleep(10)

# #select TOI,ET video  as channel and etimes,ET online as product
# Click("/html/body/div[3]/div[2]/h1/div/button/i")
# Click('//*[@id="channels"]/div/div[7]/div[2]/div/div[3]/p/span[2]/label/span')
# Click('//*[@id="channels"]/div/div[2]/div[2]/div/div[2]/p/span[2]/label/span')
# Click('//*[@id="apply"]')
# time.sleep(10)

#AllMedia
Click('/html/body/div[1]/nav/ul/li[2]/a')
Click('//*[@id="table_div"]/div/div[1]/table/tbody/tr[1]/td[2]/a')

time.sleep(15)
switchframe('//*[@id="abhimanyu"]')
print(GetTextValue('//*[@id="vrequest"]')) 
iterate=['//*[@id="vrequest"]','/html/body/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[1]/div[1]/span','/html/body/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div[1]/span','/html/body/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[3]/div[1]/span','/html/body/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[4]/div[1]/span','/html/body/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[5]/div[1]/span','//*[@id="arequest"]','/html/body/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/span','/html/body/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[1]/span','/html/body/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[3]/div[1]/span']
for i in iterate:
    if GetTextValue(i)=='0':
        print("bhai glt hai o aa rha")
        break
# Click('//*[@id="ccll"]/span')


print("done")
driver.close()




