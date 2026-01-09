from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username = "#Email"
    textbox_password = "#Password"
    button_login = ".login-button"
    button_logout_text = "Logout"
    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_username).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_username).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_password).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_password).send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_login).click()

    def clickLogoutButton(self):
        self.driver.find_element(By.LINK_TEXT, self.button_logout_text).click()