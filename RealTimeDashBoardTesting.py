from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#function to test real time dashboard
def RealTimeDashboardValidation(driver):
    #function to get the text of the given element xpath    
    def GetTextValue(xpath):    
        element = WebDriverWait(driver,40).until(
        EC.presence_of_element_located((By.XPATH,xpath))
        )
        return element.text


    #function to get the validation of a string containing number is zero or nonzero    
    def HeaderValidationHelper(str1):
        numvalue=""
        for i in  range(len(str1)):
            t=str1[i].isalpha()
            if t==False:
                numvalue=numvalue+str1[i]
        num=float(numvalue)
        if num==0.0:
            return False
        else:
            return True
    RealTimeHeader=[]
    for i in range(1,9):
        xpath='/html/body/div[3]/div[2]/div[4]/div/div[1]/div[{}]/div/div[2]'.format(i)
        RealTimeHeader.append(HeaderValidationHelper(GetTextValue(xpath).split("\n",1)[0]))
        
    print(RealTimeHeader)
    for i in range(len(RealTimeHeader)):
        if RealTimeHeader[i]==False:
            print("there is zero value into the Top header of RealTime Dashboard field")
            sys.exit() 




   # Top ProductSection Graph
    text=GetTextValue('/html/body/div[3]/div[2]/div[4]/div/div[3]/div[3]/div/div[2]/div')
    if text=="":
        print("No Graph In the Top Prodcut section")
        sys.exit()



  #  Top sections Graph
    text=GetTextValue('/html/body/div[3]/div[2]/div[4]/div/div[3]/div[3]/div/div[2]/div')
    if text=='No data':
        print("there is No graph in the Top sections Ui fiedl of real Time Dashboard")
        sys.exit()


 #   Top Browsers Graph
    text=GetTextValue('//*[@id="top-browser"]')
    if text=='No data':
        print("there is No graph in the Top Browsers Ui fiedl of real Time Dashboard")
        sys.exit()



#  Top Platforms section
    text=GetTextValue('//*[@id="top-platform"]')
    if text=='No data':
         print("there is No graph in the Top Platforms Ui fiedl of real Time Dashboard")
         sys.exit()



  #  VIDEO & AD DISTRIBUTION Graph  
    text=GetTextValue('/html/body/div[3]/div[2]/div[4]/div/div[3]/div[1]')
    text=text.split("\n")
    if text[3].find("No Data")!=-1:
        print("There is no graph in the Video & Ad Distribution section")
        sys.exit()


  #  GeoGraphical Distribution section
    text=GetTextValue('/html/body/div[3]/div[2]/div[4]/div/div[4]/div/div/div[2]/div/div[1]/div/div[2]')
    if len(text.split("\n"))==1:
        print("No data into the Geographical Distribution section")
        sys.exit()
    print("Realtime validation validation done")


   
