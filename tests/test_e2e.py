import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

#@pytest.mark.usefixtures("setup")



class TestOne(BaseClass):
    #Inheriting base class here

    def test_e2e(self):
        log = self.getLogger() # Calling Log method from BaseClass
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        log.info("getting all the cards title")
        # self.driver.find_element_by_css_selector("a[href*='shop']").click()

        # checkOutPage = CheckOutPage(self.driver)
        cards = checkOutPage.getCardTitles()
        #products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkOutPage.getCardFooter()[i].click()


        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        confirmPage = checkOutPage.checkOutItems()
        #self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        log.info("Entering country Name")
        self.driver.find_element_by_id("country").send_keys("ind")

        self.verifyLinkPresenece("India")  # Calling wait from BaseClass

        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        successText = self.driver.find_element_by_class_name("alert-success").text
        log.info("Text received is"+successText)

        assert "Success! Thank you!" in successText

        self.driver.get_screenshot_as_file("screen.png")


