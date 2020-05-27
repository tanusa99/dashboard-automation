import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from validation import VAlIDATEUIRENDERING
from RealTimeDashBoardTesting import RealTimeDashboardValidation
from allmedia import Allmedia
from selenium.common.exceptions import NoSuchElementException

# find the element with explicit wait
def GetTextValue(xpath):   
    element = WebDriverWait(driver,40).until(
    EC.presence_of_element_located((By.XPATH,xpath))
    )
    return element.text

# find the element with explicit wait and click on it
def Click(xpath):
    element = WebDriverWait(driver,40).until(
    EC.presence_of_element_located((By.XPATH,xpath))
    )
    driver.execute_script("arguments[0].click();", element)

#executable_path="C:/Users/c-nitesh.agarwal/Desktop/selenium/geckodriver"
#executable_path="/home/tanusha/Desktop/selenium/geckodriver"
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://stats.slike.in/login")  
time.sleep(10)

# login
username = driver.find_element_by_xpath('//*[@id="email"]').send_keys("slikesuper")
password = driver.find_element_by_xpath('//*[@id="password"]').send_keys(" slik3!$uper@")
driver.find_element_by_xpath('//*[@id="submitBtn"]').click()

#select TOI,ET video  as channel and etimes,ET online as product and validation
Click("/html/body/div[3]/div[2]/h1/div/button/i")
Click('//*[@id="channels"]/div/div[7]/div[2]/div/div[3]/p/span[2]/label/span')
Click('//*[@id="channels"]/div/div[2]/div[2]/div/div[2]/p/span[2]/label/span')
Click('//*[@id="apply"]')
time.sleep(10)
VAlIDATEUIRENDERING(driver)


# select yesterday as date range and check validation
Click('//*[@id="reportrange"]')
Click("/html/body/div[4]/div[1]/ul/li[1]")
VAlIDATEUIRENDERING(driver)

# All media validation and audio filter
Allmedia(driver)

# Realtime dashboard validation
Click('/html/body/div[1]/nav/ul/li[3]/a')
Click('/html/body/div[1]/nav/ul/li[3]/ul/li[1]/a/i')
RealTimeDashboardValidation(driver)

# custom report
Click("/html/body/div[1]/nav/ul/li[4]/a")
Click('//*[@id="rlItmAESEAnIBU4xD353ux_4P"]/div[1]/div/a')
# Click("/html/body/div[3]/div/div[2]/div/a[1]")
time.sleep(10)
Click("/html/body/div[3]/div/div[2]/div/a[2]")
time.sleep(10)
Click("/html/body/div[3]/div[2]/div/div/button[3]")
time.sleep(10)
print("Done")
driver.close()




