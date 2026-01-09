from selenium.webdriver.common.by import By


class AddCustomer:
    lnkCustomers_menu_xpath = "//nav/ul/li[4]"
    lnkCustomers_menuitem_xpath = "//nav/ul/li[4]/ul/li[1]"
    btnAddnew_xpath = "//a[@href='/Admin/Customer/Create']"
    txtEmail_css = "#Email"
    txtPassword_css = "#Password"
    txtFirstName_css = "#FirstName"
    txtLastName_css = "#LastName"
    rdMaleGender_css = "#Gender_Male"
    rdFemaleGender_css = "#Gender_Female"
    txtCompanyName_css = "#Company"
    txtAdminContent_css = "#AdminComment"
    btnSave_xpath = "//button[@name='save']"
    def __init__(self, driver):
        self.driver = driver
    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddNewCustomerPage(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.CSS_SELECTOR, self.txtEmail_css).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.CSS_SELECTOR, self.txtPassword_css).send_keys(password)

    def setFirstName(self, firstname):
        self.driver.find_element(By.CSS_SELECTOR, self.txtFirstName_css).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.CSS_SELECTOR, self.txtLastName_css).send_keys(lastname)

    def setGender(self):
        self.driver.find_element(By.CSS_SELECTOR, self.rdMaleGender_css).click()

    def setCompanyName(self, companyname):
        self.driver.find_element(By.CSS_SELECTOR, self.txtCompanyName_css).send_keys(companyname)

    def setAdminContent(self, content):
        self.driver.find_element(By.CSS_SELECTOR, self.txtAdminContent_css).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()
