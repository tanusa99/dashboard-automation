import sys
import time
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from validation import VAlIDATEUIRENDERING
from RealTimeDashBoardTesting import RealTimeDashboardValidation
from selenium.common.exceptions import NoSuchElementException
def Allmedia(driver):
    def GetTextValue(xpath):   
        element = WebDriverWait(driver,40).until(
        EC.presence_of_element_located((By.XPATH,xpath))
        )
        return element.text
    def Click(xpath):
        element = WebDriverWait(driver,40).until(
        EC.presence_of_element_located((By.XPATH,xpath))
        )
        driver.execute_script("arguments[0].click();", element)

    def switchframe(xpath):
        element = WebDriverWait(driver,40).until(
        EC.presence_of_element_located((By.XPATH,xpath))
        )
        driver.switch_to.frame("abhimanyu")
    
    Click('/html/body/div[1]/nav/ul/li[2]/a')
    Click('//*[@id="table_div"]/div/div[1]/table/tbody/tr[1]/td[2]/a')
    time.sleep(15)
    switchframe('//*[@id="abhimanyu"]')
    iterate=['//*[@id="vrequest"]','/html/body/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[1]/div[1]/span','/html/body/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div[1]/span','/html/body/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[3]/div[1]/span','/html/body/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[4]/div[1]/span','/html/body/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[5]/div[1]/span','//*[@id="arequest"]','/html/body/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/span','/html/body/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[1]/span','/html/body/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[3]/div[1]/span']
    for i in iterate:
        if GetTextValue(i)=='0':
            print("Error")
            break
    #graph validation:-----
    try:
        videlement=driver.find_element_by_xpath('//*[@id="g-addiv"]')
    except NoSuchElementException:
        print("Video graph not found")
    driver.switch_to_default_content()
    Click('//*[@id="ccll"]/span')

    #Applying the audio filter
    Click('/html/body/div[3]/div[2]/h1/div/button')
    time.sleep(5)
    Click('//*[@id="exampleModalCenter"]/div/div/div[2]/div/div[1]/ul[2]/li[2]/label')
    time.sleep(5)
    Click('//*[@id="apply"]')
    time.sleep(10)
    Click('//*[@id="table_div"]/div/div[1]/table/tbody/tr[1]/td[2]/a')
    time.sleep(15)
    switchframe('//*[@id="abhimanyu"]')
    listofaudio=['//*[@id="vrequest"]','/html/body/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[1]/div[1]/span','/html/body/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div[1]/span','/html/body/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div[1]/span','/html/body/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[4]/div[1]/span','/html/body/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[5]/div[1]/span']
    for audio in listofaudio:
        if GetTextValue(audio)=='0':
            print("Error")
            break

    #graphvalidation----
    try:
        element=driver.find_element_by_xpath('//*[@id="graphData"]')
    except NoSuchElementException:
        print("Graph not found")
    driver.switch_to_default_content()
    Click('//*[@id="ccll"]/span')
