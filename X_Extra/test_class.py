from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class googleSearch():
    def  searching(self):
        baseUrl = "https:www.google.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        time.sleep(2)

        googlesearch=driver.find_element(By.CLASS_NAME,"gLFyf.gsfi")
        googlesearch.send_keys("Tintash")
        googlesearch.submit()
        time.sleep(2)

        websiteLink=driver.find_element(By.XPATH,"//h3[contains(text(),'Tintash - Stanford Alumni Led Web & App Developmen')]").click()
        time.sleep(2)

        findportfolio=driver.find_element(By.XPATH,"//div[@id='navbarToggler']/ul//a[@href='/portfolio/']").click()
        time.sleep(2)


        scrollElement = driver.find_element(By.CSS_SELECTOR, "#gatsby-focus-wrapper [class='py-5']:nth-child(3) .row")
        driver.execute_script("arguments[0].scrollIntoView(true);", scrollElement)
        driver.execute_script("window.scrollBy(0, -200);")
        time.sleep(2)

        textToSelect1 = "Web Development"
        dropdownselection = driver.find_element(By.XPATH,"//div[@id='gatsby-focus-wrapper']/section[@class='py-5']/div[2]/div[@class='container']/div/div[1]/div/div[2]/div/div[1]").click()
        ulElement = driver.find_element(By.CLASS_NAME, "css-ck91yh-menu")
        time.sleep(2)
        getelement = driver.find_element(By.ID, "react-select-2-option-1").click()
        time.sleep(2)
        dropdownselection2 = driver.find_element(By.XPATH,"//div[@id='gatsby-focus-wrapper']/section[@class='py-5']/div[2]/div[@class='container']/div/div[2]/div/div[2]/div/div[1]").click()
        oneElement = driver.find_element(By.CLASS_NAME, "css-ck91yh-menu")
        Elements2 = oneElement.find_elements(By.TAG_NAME, "div")
        time.sleep(2)
        textToSelect2 = "ReactJS"
        for element in Elements2:
            if textToSelect2 in element.text:
                element.click()
                break
        time.sleep(2)

        dropdownselection3 = driver.find_element(By.XPATH, "//div[@id='gatsby-focus-wrapper']/section[@class='py-5']/div[2]/div[@class='container']/div/div[3]/div/div[2]/div/div[1]").click()
        oneElement = driver.find_element(By.CLASS_NAME, "css-ck91yh-menu")
        time.sleep(2)
        getelement = driver.find_element(By.ID, "react-select-4-option-13").click()
        time.sleep(2)

        findCamaradly = driver.find_element(By.XPATH, "//div[contains(text(),'Camaradly is an employee-first feedback, engagemen')]")
        if findCamaradly != False:
            print("Camaradly exists")
        else:
            print("Camaradly Doesn't exists")

        time.sleep(2)

        driver.quit()

test1=googleSearch()
test1.searching()