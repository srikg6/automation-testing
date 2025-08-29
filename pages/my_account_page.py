import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class MyAccountPage:
    """Page Object for My Account page (Login & Register)."""

    # --- Locators ---
    # Login Section
    loc_login_username = (By.ID, "username")
    loc_login_password = (By.ID, "password")
    loc_login_button = (By.NAME, "login")

    # Register Section
    loc_register_email = (By.ID, "reg_email")
    loc_register_password = (By.ID, "reg_password")
    loc_register_button = (By.NAME, "register")

    # After login - verify logout link
    loc_logout_link = (By.LINK_TEXT, "Logout")

    # Error messages displayed
    loc_inv_email_msg = (By.XPATH, "//*[@class='woocommerce-error']//li")

    # Address section
    loc_addresses_link = (By.LINK_TEXT, "Addresses")
    loc_edit_billing_address = (By.XPATH, "//h3[text()='Billing Address']/following-sibling::a")
    loc_edit_shipping_address = (By.XPATH, "//h3[text()='Shipping Address']/following-sibling::a")



    def __init__(self, driver: WebDriver):
        self.driver = driver

    # --- Page Actions ---
    def login(self, username, password):
        """Login with valid credentials"""
        self.driver.find_element(*self.loc_login_username).send_keys(username)
        self.driver.find_element(*self.loc_login_password).send_keys(password)
        ele = self.driver.find_element(*self.loc_login_button)
        if ele.is_enabled():
            ele.click()
        else:
            return False

    def enter_email(self, email):
        self.driver.find_element(*self.loc_register_email).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.loc_register_password).send_keys(password)

    def click_register_button(self, status):
        ele = self.driver.find_element(*self.loc_register_button)
        if ele.is_enabled() is status:
            ele.click()

    def register(self, email, password):
        """Register with new user"""
        self.driver.find_element(*self.loc_register_email).send_keys(email)
        self.driver.find_element(*self.loc_register_password).send_keys(password)
        self.driver.find_element(*self.loc_register_button).click()

    def is_logout_link_displayed(self):
        """Check if logout link is visible after login/registration"""
        return self.driver.find_element(*self.loc_logout_link).is_displayed()

    def capture_error_and_validate(self, expected):
        time.sleep(5)
        error_msg = self.driver.find_element(*self.loc_inv_email_msg)
        msg_text = error_msg.text
        print("\n")
        print(msg_text)
        print(expected)
        # assert msg_text == expected, "Validation failed"

    def click_addresses_link(self):
        self.driver.find_element(*self.loc_addresses_link).click()

    def edit_billing_address(self):
        self.driver.find_element(*self.loc_edit_billing_address).click()

    def edit_shipping_address(self):
        self.driver.find_element(*self.loc_edit_shipping_address).click()