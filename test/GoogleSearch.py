from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Users\\admin\\Desktop\\Automation 2019-2020\\downloads\\chrome\\chromedriver.exe")
#driver = webdriver.Ie("C:\\Users\\admin\\Desktop\\Automation 2019-2020\\downloads\\ie\\IEDriverServer.exe")
driver.maximize_window()
driver.get("https://www.google.com/")
driver.implicitly_wait(30)
print("page title is: ", driver.title)

assert "Google" in driver.title
searchBox=driver.find_element_by_name("q")
searchBox.send_keys("India")
searchBtn=driver.find_element_by_name("btnK")
searchBtn.click()
time.sleep(3)
driver.get_screenshot_as_file("google.png")
driver.quit()