from selenium import webdriver
from pages.homepage2 import DragAndDrop
import unittest


class Testing1(unittest.TestCase):
    baseUrl = "https://jqueryui.com/droppable/"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(baseUrl)
    driver.implicitly_wait(5)

class test_dragAnddrop(Testing1):

        def testdragdrop(self):

                dd = DragAndDrop(self.driver)
                tc1 = dd.switchframe(0)
                tc1 = dd.draganddroptest()


                """
                 #baseUrl = "https://jqueryui.com/droppable/"
                #sd = SeleniumDriver()
                #self.driver = sd.getDriver(baseUrl)
                #print(self.driver)
                
                
                baseUrl = "https://jqueryui.com/droppable/"
                 sd=SeleniumDriver()
                self.driver=sd.getDriver(baseUrl)
                 print(self.driver)


                 driver = webdriver.Chrome()

                driver.maximize_window()
                driver.get(baseUrl)
                driver.implicitly_wait(5)
                 """








