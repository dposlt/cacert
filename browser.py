from selenium import webdriver
import time

driver = webdriver.Chrome(r"R:\wwwroot\cacert\chromedriver_win32\chromedriver.exe") ## need absolute path
def generateCert(pastetext):


    weburl = 'https://ica/certsrv/certrqxt.asp'
    if driver:
        driver.get(weburl)

        #insert hash to textarea
        textarea = driver.find_element_by_id("locTaRequest")
        textarea.clear()
        textarea.send_keys(pastetext)

        #change columb
        selector = driver.find_element_by_id("lbCertTemplateID")

        [doubleclick for i in range(2) if selector.click()] #doubleclick

        driver.find_element_by_id("btnSubmit").click()

        #change radio
        radio = driver.find_element_by_id("locB64Enc0")
        radio.click()

        #download cert
        driver.find_element_by_link_text("Download certificate").click()
        time.sleep(5) #waiting for download


    else:
        print('driver not found')
        exit()


def close():
    driver.close()
