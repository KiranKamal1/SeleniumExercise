from selenium import webdriver
from pages.homepage import homepage
import time
import unittest

class Testing(unittest.TestCase):
    baseUrl = "https:www.google.com"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(baseUrl)
    driver.implicitly_wait(5)

class test_googlesearch(Testing):

    def testgoogleSearchTC(self):
        #driver = SeleniumDriver()
        gs=homepage(self.driver)

        tc = gs.findgooglesearch("Tintash")
        tc = gs.websitelink()
        tc = gs.portfolio()
        tc = gs.scrollElement()
        tc = gs.dropdownSelection1()
        tc = gs.dropdownSelection2()
        tc = gs.dropdownSelection3()
        tc = gs.findCamaradlytest()

        time.sleep(3)

        self.driver.quit()






















