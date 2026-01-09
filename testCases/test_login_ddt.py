from time import sleep

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customerLogger import LogGen
from utilities import XLUtils

class Test_001_DDT_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    path = ".//testData/LoginData.xlsx"

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("********Testing Login Page Title********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows: ", self.rows)
        lst_status = []
        for i in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1', i, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', i, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', i, 3)
            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLoginButton()
            sleep(3)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info("*** Result: Passed (Expected Pass & Got Pass) ***")
                    self.lp.clickLogoutButton()
                    lst_status.append("Pass")
                elif self.exp == 'Fail':
                    self.logger.info("*** Result: Failed (Expected Fail but Got Pass) ***")
                    self.lp.clickLogoutButton()
                    lst_status.append("Fail")
            else:
                if self.exp == 'Pass':
                    self.logger.info("*** Result: Failed (Expected Pass but Got Fail) ***")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("*** Result: Passed (Expected Fail & Got Fail) ***")
                    lst_status.append("Pass")

            if "Fail" not in lst_status:
                self.logger.info("******* DDT Login Test Passed *******")
                assert True
            else:
                self.logger.error("******* DDT Login Test Failed *******")
                assert False
