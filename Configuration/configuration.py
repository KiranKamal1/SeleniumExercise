from selenium import webdriver
import unittest



class SeleniumDriver(object):

    def __init__(self):
        """
        baseUrl = "https:www.google.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)
        """

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://google.com")



    def getDriver(self,baseUrl):
        print("*#"*10)
        try:
            print(self.driver.current_url)
            driver=self.driver.get(baseUrl)
            print(driver)
            return driver

        except Exception as err:
            print("error has ocurred")
        print("*#" * 10)

"""

def getDriver(self):
        baseUrl = "https:www.google.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)
        return driver

#def getUrl(self, url):
  #self.driver.get(url)

def base_Url(self,url):
    baseUrl = "https:www.google.com"


class changedriver(SeleniumDriver):
def __init__(self):
    SeleniumDriver.__init__(self)

def base_Url(self,url):
    self.url=url

"""







