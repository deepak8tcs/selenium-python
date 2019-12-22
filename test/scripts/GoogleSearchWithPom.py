from selenium import webdriver
import time
import unittest
from main.pages.HomePage import HomePage



class GoogleSearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:/Users/admin/Desktop/Automation 2019-2020/downloads/chrome/chromedriver.exe")
        # driver = webdriver.Ie("C:\\Users\\admin\\Desktop\\Automation 2019-2020\\downloads\\ie\\IEDriverServer.exe")
        cls.driver.maximize_window()
        cls.driver.get("https://www.google.com/")
        cls.driver.implicitly_wait(30)
        # cls.homePage = HomePage(cls.driver)

    def test_search(self):
        self.homePage = HomePage(self.driver)
        print("page title is: ", self.driver.title)
        self.assertEqual("xyz", "xyz", "mistmatch occured")
        self.assertTrue(True, "failed assertion")
        assert "Google" in self.driver.title
        self.homePage.enterSearchText("USA")
        self.homePage.clickSearchBtn()
        time.sleep(3)
        # driver.get_screenshot_as_file("google.png")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


#if __name__ == '__main()__':
   # unittest.main(testRunner= HtmlTestRunner.HtmlTestRunner(outut= "C:/Users/admin/PycharmProjects/selenium-python/reports"))
