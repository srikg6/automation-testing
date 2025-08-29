from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    """Page Object for Home Page top navigation bar"""
    # Locators
    loc_shop_link = (By.LINK_TEXT, "Shop")
    loc_my_account_link = (By.LINK_TEXT, "My Account")
    loc_addresses = (By.LINK_TEXT, "Addresses")
    loc_test_cases_link = (By.LINK_TEXT, "Test Cases")
    loc_at_site_link = (By.LINK_TEXT, "AT Site")
    loc_demo_site_link = (By.LINK_TEXT, "Demo Site")
    loc_cart_link = (By.CLASS_NAME, "cartcontents")  # cart text
    loc_cart_amount = (By.CLASS_NAME, "amount")      # ₹0.00 element

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_shop(self):
        self.wait.until(EC.element_to_be_clickable(self.loc_shop_link)).click()

    def click_my_account(self):
        self.wait.until(EC.element_to_be_clickable(self.loc_my_account_link)).click()

    def click_addresses(self):
        self.wait.until(EC.element_to_be_clickable(self.loc_addresses)).click()

    def click_test_cases(self):
        self.wait.until(EC.element_to_be_clickable(self.loc_test_cases_link)).click()

    def click_at_site(self):
        self.wait.until(EC.element_to_be_clickable(self.loc_at_site_link)).click()

    def click_demo_site(self):
        self.wait.until(EC.element_to_be_clickable(self.loc_demo_site_link)).click()

    def get_cart_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.loc_cart_link)).text

    def get_cart_amount(self):
        return self.wait.until(EC.visibility_of_element_located(self.loc_cart_amount)).text
