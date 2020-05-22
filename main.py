import sys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# find the element with explicit wait
def Click(xpath):
    element = WebDriverWait(driver,40).until(
    EC.presence_of_element_located((By.XPATH,xpath))
    )
    element.click()

    

#executable_path="C:/Users/c-nitesh.agarwal/Desktop/selenium/geckodriver"
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://stats.slike.in/login")  
time.sleep(2)

# login
username = driver.find_element_by_xpath('//*[@id="email"]').send_keys("slikesuper")
password = driver.find_element_by_xpath('//*[@id="password"]').send_keys(" slik3!$uper@")
driver.find_element_by_xpath('//*[@id="submitBtn"]').click()
time.sleep(20)

#select TOI,ET video  as channel and etimes,ET online as product
Click("/html/body/div[3]/div[2]/h1/div/button/i")
Click('//*[@id="channels"]/div/div[7]/div[2]/div/div[3]/p/span[2]/label/span')
Click('//*[@id="channels"]/div/div[2]/div[2]/div/div[2]/p/span[2]/label/span')
Click('//*[@id="apply"]')
time.sleep(10)

#function to verify the complete window ui rendering step3
#Validation()

print("done")
driver.close()


