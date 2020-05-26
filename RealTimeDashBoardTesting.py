import sys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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



#function to check the result if 0 or nonzero
def checkZeroOrNonzeroValue(checklist):
    for i in range(len(checklist)):
        if checklist[i]==False:
            print("there is zero value into the Top header field")
            sys.exit()     
         




#function to check the validation of the header top of the page
def HeaderValidation():
    resultTopHeader=[]
    for i in range(1,9):
           xpath='//*[@id="funel"]/div/div[{}]/div/div[2]'.format(i)      
           res=HeaderValidationHelper(GetTextValue(xpath).split("\n",1)[0])
           resultTopHeader.append(res)
    print(resultTopHeader)#after remove
    checkZeroOrNonzeroValue(resultTopHeader)
   



def AddJourneyValidation():
    addjourney=[]
    addjourney.append(HeaderValidationHelper(GetTextValue('//*[@id="ajourney"]/div/div/div[2]/div/ul/li[1]/p/span')))
    addjourney.append(HeaderValidationHelper(GetTextValue('//*[@id="ajourney"]/div/div/div[2]/div/ul/li[3]/ul/li/div/span')))
    for i in range(2,8):
        xpath='//*[@id="ajourney"]/div/div/div[2]/div/ul/li[{}]/div/span'.format(i)
        res=HeaderValidationHelper(GetTextValue(xpath))
        addjourney.append(res)
    print(addjourney)
    checkZeroOrNonzeroValue(addjourney)







def VideoJourneyValidation():
     videojourney=[]
     videojourney.append(HeaderValidationHelper(GetTextValue('//*[@id="vjourney"]/div/div/div[2]/div[2]/ul/li[1]/ul/li/div/span')))
     videojourney.append(HeaderValidationHelper(GetTextValue('//*[@id="vjourney"]/div/div/div[2]/div[2]/ul/li[1]/p[2]/span')))
     videojourney.append(HeaderValidationHelper(GetTextValue('//*[@id="vjourney"]/div/div/div[2]/div[2]/ul/li[4]/ul/li/div/span')))
     videojourney.append(HeaderValidationHelper(GetTextValue('//*[@id="vjourney"]/div/div/div[2]/div[2]/ul/li[6]/ul/li/div/span')))
     for i in range(2,10):
        xpath='//*[@id="vjourney"]/div/div/div[2]/div[2]/ul/li[{}]/div/span'.format(i)
        res=HeaderValidationHelper(GetTextValue(xpath))
        videojourney.append(res)
     print(videojourney)
     checkZeroOrNonzeroValue(videojourney)







def GEOGRAPHICALDISTRIBUTION():
    res1=GetTextValue('//*[@id="GEO_1"]/tbody/tr[1]/td[1]')
    text='No data available in table'
    if(res1==text):
        print("No data In GEOGRAPHICALDISTRIBUTION Table ")
        sys.exit()







def ADAndVIDEODISTRIBUTION():
    text=GetTextValue('//*[@id="ad_distribution"]/div')
    if text=="":
       print("No graph shown On ADAndVIDEODISTRIBUTION( section")
       sys.exit()
        





def ENGAGEMENTValidation():
    for i in range(1,8):
        xpath='//*[@id="advidavg"]/div/div/div/div[2]/div[1]/ul/li[{}]'.format(i)
        text=GetTextValue(xpath).split('\n')
        if text[1]=='0:00':
            print(text[0]+"value is "+text[1]+'shown in the engagementsection')
            sys.exit()
        if text[1]=='NaN%':
            print(text[0]+"value is "+text[1]+'shown in the engagementsection')
            sys.exit()
        if text[1]=='NaN':
            print(text[0]+"value is "+text[1]+'shown in the engagementsection')
            sys.exit()
            
    
    text=GetTextValue('//*[@id="hh"]')
    graphvalidtext='(%viewd)'
    if text== graphvalidtext:
        print("No Graph Shown For ENGAGEMENT section")
        sys.exit()





def TOPPERFORMINGValidation():
     text=GetTextValue('//*[@id="TABLE_3_wrapper"]/div[1]')
     if text.find('No data available in table')!=-1:
         print("there is no viedo shown in Top performing section on ui")
         sys.exit()






def AVERAGELOADTIMEValidation():
      for i in range(1,4):
          xpath='//*[@id="f_loadtime"]/div/div/div/div[2]/div/ul/li[{}]'.format(i)
          text=GetTextValue(xpath).split("\n")
          if HeaderValidationHelper(text[1])==False:
              print(text[0]+"value is shown 0 on ui")
              sys.exit()
        



def Validation():
    HeaderValidation()
    ADAndVIDEODISTRIBUTION()
    ENGAGEMENTValidation()
    VideoJourneyValidation()
    AddJourneyValidation()
    GEOGRAPHICALDISTRIBUTION()
    AVERAGELOADTIMEValidation()
    TOPPERFORMINGValidation()
    


#function to test real time dashboard
def RealTimeDashboardValidation():
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
   


   
