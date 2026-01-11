from time import sleep
import random
import string
import pytest
from selenium.webdriver.common.by import By

from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customerLogger import LogGen
from utilities import XLUtils

class Test_003_AddCustomer:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    path = ".//testData/LoginData.xlsx"

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addCustomer(self, setup):
        self.logger.info("********Testing AddCustomer********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLoginButton()

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        sleep(4)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        self.addcust.clickOnAddNewCustomerPage()
        generated_email = random_generator(8) + "@gmail.com"
        self.addcust.setEmail(generated_email)
        self.addcust.setPassword("123123")
        self.addcust.setFirstName("David")
        self.addcust.setLastName("Lawrence")
        self.addcust.setGender()
        self.addcust.setCompanyName("Prize")
        self.addcust.setAdminContent("any")
        self.addcust.clickOnSave()
        sleep(2)
        # self.driver.close()

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        if 'customer has been added successfully' in self.msg:
            assert True == True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"/addCustomer.png")
            assert True == False

def random_generator(size=8, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))



