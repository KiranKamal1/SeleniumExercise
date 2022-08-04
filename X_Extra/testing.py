from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class testing():
    def testingtheflow(self):
        baseUrl = "https://tintash.com/portfolio/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        time.sleep(2)

        scrollElement = driver.find_element(By.ID, "react-select-2-input")
        driver.execute_script("arguments[0].scrollIntoView(true);", scrollElement)
        driver.execute_script("window.scrollBy(0, -200);")
        time.sleep(2)

        #dropdownselection = driver.find_element(By.XPATH,"//div[contains(@class=’css-1hwfws3') and contains(text()='Select Solution')]]").click()
        dropdownselection = driver.find_element(By.XPATH,"//div[@id='gatsby-focus-wrapper']/section[@class='py-5']/div[2]/div[@class='container']/div/div[1]/div/div[2]/div/div[1]").click()
        time.sleep(2)

        ulElement = driver.find_element(By.CLASS_NAME, "css-ck91yh-menu")

        #inner_html = ulElement.get_attribute("innerHTML")
       # print(inner_html)

        getelement=driver.find_element(By.ID,"react-select-2-option-1").click()
        time.sleep(2)
        
        dropdownselection2 = driver.find_element(By.XPATH,"//div[@id='gatsby-focus-wrapper']/section[@class='py-5']/div[2]/div[@class='container']/div/div[2]/div/div[2]/div/div[1]").click()
        time.sleep(2)

        ulElement = driver.find_element(By.CLASS_NAME, "css-ck91yh-menu")

        #inner_html = ulElement.get_attribute("innerHTML")
        #print(inner_html)

        liElements = ulElement.find_elements(By.TAG_NAME, "div")
        time.sleep(2)
        textToSelect="ReactJS"
        for element in liElements:
          #print(element.text)

           if textToSelect in element.text:
                element.click()
                break

        #getelement=driver.find_element(By.ID,"react-select-2-option-1").click()
        time.sleep(2)

        dropdownselection3 = driver.find_element(By.XPATH,"//div[@id='gatsby-focus-wrapper']/section[@class='py-5']/div[2]/div[@class='container']/div/div[3]/div/div[2]/div/div[1]").click()
        time.sleep(2)

        ulElement = driver.find_element(By.CLASS_NAME, "css-ck91yh-menu")
        getelement = driver.find_element(By.ID, "react-select-4-option-13").click()
        #inner_html = ulElement.get_attribute("innerHTML")
       # print(inner_html)

        liElements = ulElement.find_elements(By.TAG_NAME, "div")
        time.sleep(2)
        textToSelect = "Workplace Experience & Management"
        for element in liElements:
            #print(element.text)

            if textToSelect in element.text:
                element.click()
                break
        time.sleep(2)



            #print(element.text)

            #if textToSelect in element.text:
             #   driver.execute_script("arguments[0].scrollIntoView(true);", element)
             #   location = element.location_once_scrolled_into_view
             #   element.click()
             #   break

        # getelement=driver.find_element(By.ID,"react-select-2-option-1").click()
        time.sleep(2)
        findCamaradly=driver.find_element(By.XPATH,"//div[contains(text(),'Camaradly is an employee-first feedback, engagemen')]")
        if findCamaradly!=False:
            print("Camaradly exists")
        else:
            print("Camaradly Doesn't exists")

        time.sleep(2)



t=testing()
t.testingtheflow()