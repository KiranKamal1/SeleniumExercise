from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import unittest

class DragAndDrop(unittest.TestCase):

    def test1(self):
        baseUrl = "https://jqueryui.com/droppable/"
        driver = webdriver.Chrome()
        #driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        driver.switch_to.frame(0)

        fromElement = driver.find_element(By.ID, "draggable")
        toElement = driver.find_element(By.ID, "droppable")
        time.sleep(2)
        try:
            actions = ActionChains(driver)
            actions.drag_and_drop(fromElement, toElement).perform()
            print("Drag And Drop Element Successful")
            time.sleep(2)
        except:
            print("Drag And Drop failed on element")

#ff = DragAndDrop()
#ff.test1()
if __name__ == '__main__':
    unittest.main()