from selenium.webdriver import ActionChains
from Locators.pagelocator import draganddroplocator
from selenium.webdriver.common.by import By

class DragAndDrop(object):

    def __init__(self,driver):
        self.driver=driver

    def switchframe(self,a):
        #print(self.driver)
        self.driver.switch_to.frame(a)

    def draganddroptest(self):
        fromElement = self.driver.find_element(By.ID,draganddroplocator.draglocator)
        toElement = self.driver.find_element(By.ID, draganddroplocator.droplocator)
        try:
            actions = ActionChains(self.driver)
            actions.drag_and_drop(fromElement, toElement).perform()
            print("Drag And Drop Element Successful")
        except:
            print("Drag And Drop failed on element")

        self.driver.quit()