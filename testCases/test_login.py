from time import sleep

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customerLogger import LogGen

class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("********Testing Home Page Title********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        assert act_title == "nopCommerce demo store. Login"
        self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
        self.driver.close()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("********Testing Login Page Title********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        sleep(2)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLoginButton()
        act_title = self.driver.title
        assert act_title == "Dashboard / nopCommerce administration"
        self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
        self.driver.close()
