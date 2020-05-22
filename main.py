from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# find the element with explicit wait and click on it
def Click(xpath):
    element = WebDriverWait(driver,40).until(
    EC.presence_of_element_located((By.XPATH,xpath))
    )
    driver.execute_script("arguments[0].click();", element)



driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://stats.slike.in/login")  


# login
username = driver.find_element_by_xpath('//*[@id="email"]').send_keys("slikesuper")
password = driver.find_element_by_xpath('//*[@id="password"]').send_keys(" slik3!$uper@")
driver.find_element_by_xpath('//*[@id="submitBtn"]').click()

#select TOI,ET video  as channel and etimes,ET online as product
Click("/html/body/div[3]/div[2]/h1/div/button/i")
Click('//*[@id="channels"]/div/div[7]/div[2]/div/div[3]/p/span[2]/label/span')
Click('//*[@id="channels"]/div/div[2]/div[2]/div/div[2]/p/span[2]/label/span')
Click('//*[@id="apply"]')

# select yesterday as date range and check validation
Click('//*[@id="reportrange"]')
Click("/html/body/div[4]/div[1]/ul/li[1]")



# custom report

Click("/html/body/div[1]/nav/ul/li[4]/a")
Click('//*[@id="rlItmAESEAnIBU4xD353ux_4P"]/div[1]/div/a')
# Click("/html/body/div[3]/div/div[2]/div/a[1]")
time.sleep(5)
Click("/html/body/div[3]/div/div[2]/div/a[2]")
time.sleep(5)
Click("/html/body/div[3]/div[2]/div/div/button[3]")
time.sleep(10)
print("done")
driver.close()

