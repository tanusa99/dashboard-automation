from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path="/home/tanusha/Desktop/selenium/geckodriver")
driver.maximize_window()
driver.get("https://stats.slike.in/login")  
time.sleep(2)
username = driver.find_element_by_xpath('//*[@id="email"]').send_keys("slikesuper")
password = driver.find_element_by_xpath('//*[@id="password"]').send_keys(" slik3!$uper@")
driver.find_element_by_xpath('//*[@id="submitBtn"]').click()
time.sleep(10)
driver.find_element_by_xpath('/html/body/div[3]/div[2]/h1/div/button/i').click()
driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div/div[3]/div/ul/li[112]/label').click()
driver.find_element_by_xpath('//*[@id="apply"]').click()