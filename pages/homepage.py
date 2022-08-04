from selenium.webdriver.common.by import By
from Locators.pagelocator import websiteLocators
from Locators.pagelocator import websiteLocatorType
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC


class homepage(object):

    def __init__(self,driver):
        self.driver=driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            return False

    def findgooglesearch(self,text):
        byType = self.getByType(websiteLocatorType.googlesearchlocatorType)
        googlesearch = self.driver.find_element(byType, websiteLocators.googlesearchlocator)
        googlesearch.send_keys(text)
        googlesearch.submit()

    def websitelink(self):
        byType = self.getByType(websiteLocatorType.websitelinklocatorType)
        self.driver.find_element(byType,websiteLocators.websitelinklocator).click()

    def portfolio(self):
        byType = self.getByType(websiteLocatorType.findportfoliolocatorType)
        self.driver.find_element(byType,websiteLocators.findportfoliolocator).click()

    def scrollElement(self):
        byType = self.getByType(websiteLocatorType.scrollElementlocatorType)
        scrolling=self.driver.find_element(byType,websiteLocators.scrollElementlocator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scrolling)
        self.driver.execute_script("window.scrollBy(0, -200);")

    def dropdownSelection1(self):
        byType = self.getByType(websiteLocatorType.dropdownselectionlocatorType)
        self.driver.find_element(byType,websiteLocators.dropdownselectionlocator).click()
        byType = self.getByType(websiteLocatorType.dropdownFieldlocatorType)
        self.driver.find_element(byType, websiteLocators.dropdownFieldlocator)
        byType = self.getByType(websiteLocatorType.dropdownElement1LocatorType)
        self.driver.find_element(byType, websiteLocators.dropdownElement1Locator).click()



    def dropdownSelection2(self):
        byType = self.getByType(websiteLocatorType.dropdownselection2locatorType)
        self.driver.find_element(byType, websiteLocators.dropdownselection2locator).click()
        byType = self.getByType(websiteLocatorType.dropdownFieldlocatorType)
        Menu=self.driver.find_element(byType, websiteLocators.dropdownFieldlocator)
        Elements2 = Menu.find_elements(By.TAG_NAME, "div")
        textToSelect2 = "ReactJS"
        for element in Elements2:
            if textToSelect2 in element.text:
                element.click()
                break


    def dropdownSelection3(self):
        byType = self.getByType(websiteLocatorType.dropdownselection3locatorType)
        self.driver.find_element(byType, websiteLocators.dropdownselection3locator).click()
        byType = self.getByType(websiteLocatorType.dropdownFieldlocatorType)
        self.driver.find_element(byType, websiteLocators.dropdownFieldlocator)
        byType = self.getByType(websiteLocatorType.dropdownElement3LocatorType)
        el=self.driver.find_element(By.ID, websiteLocators.dropdownElement3Locator)
        self.driver.execute_script("arguments[0].click();", el)

     #   element=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((byType, websiteLocators.dropdownElement3Locator)))
      #  element.click()


    def findCamaradlytest(self):
        byType = self.getByType(websiteLocatorType.findCamaradlylocatorType)
        findCamradly=self.driver.find_element(byType,websiteLocators.findCamaradlylocator)
        if findCamradly!=False:
            print("Camaradly exists")
        else:
            print("Camaradly Doesn't exists")

