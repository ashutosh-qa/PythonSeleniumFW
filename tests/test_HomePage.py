import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmittion(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("First name is"+getData["Fname"])
        homepage.getName().send_keys(getData["Fname"])
        homepage.getEmail().send_keys(getData["Lname"])
        homepage.getCheckbox().click()
        self.selectOptionByText(homepage.getDropdown(), getData["Gender"])
        homepage.submitForm().click()
        print(homepage.getMessage().text)
        alertText = homepage.getMessage().text
        assert ("success" in alertText)
        self.driver.refresh()

    #@pytest.fixture(params=HomePageData.test_HomePage_data)
    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param
