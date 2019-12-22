class HomePage:

    def __init__(self, driver):
        self.driver=driver
        self.searchBox_name = "q"
        self.searchBtn_name = "btnK"

    def enterSearchText(self, searchText):
        self.driver.find_element_by_name(self.searchBox_name).send_keys(searchText)

    def clickSearchBtn(self):
        self.driver.find_element_by_name(self.searchBtn_name).click()
