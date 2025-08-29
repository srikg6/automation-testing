from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BillingAddressPage:
    # Locators
    loc_first_name = (By.ID, "billing_first_name")
    loc_last_name = (By.ID, "billing_last_name")
    loc_company = (By.ID, "billing_company")
    loc_email = (By.ID, "billing_email")
    loc_phone = (By.ID, "billing_phone")
    loc_country = (By.ID, "billing_country")
    loc_address = (By.CSS_SELECTOR, "input#billing_address_1")
    loc_address1 = (By.CSS_SELECTOR, "#billing_address_2_field")
    loc_city = (By.ID, "billing_city")
    loc_state = (By.ID, "s2id_billing_state")
    loc_postal_code = (By.ID, "billing_postcode")
    loc_save_btn = (By.NAME, "save_address")
    loc_error_msg = (By.XPATH, "//*[@id='page-36']/div/div[1]/ul/li[1]")
    loc_success_msg = (By.XPATH, "//*[@id='page-36']/div/div[1]/div[1]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Actions
    def enter_first_name(self, first_name):
        self.wait.until(EC.presence_of_element_located(self.loc_first_name)).clear()
        self.driver.find_element(*self.loc_first_name).send_keys(first_name)

    def get_first_name(self, first_name):
        text = self.wait.until(EC.presence_of_element_located(self.loc_first_name)).text
        print(f"*** {text}")
        assert text == first_name, "Value displayed in First Name field doesn't meet the expected value"

    def enter_last_name(self, last_name):
        self.wait.until(EC.presence_of_element_located(self.loc_last_name)).clear()
        self.driver.find_element(*self.loc_last_name).send_keys(last_name)

    def enter_company(self, company):
        self.driver.find_element(*self.loc_company).send_keys(company)

    def enter_email(self, email):
        self.wait.until(EC.presence_of_element_located(self.loc_email)).clear()
        self.driver.find_element(*self.loc_email).send_keys(email)

    def enter_phone(self, phone):
        self.wait.until(EC.presence_of_element_located(self.loc_phone)).clear()
        self.driver.find_element(*self.loc_phone).send_keys(phone)

    def select_country(self, country):
        dropdown = self.wait.until(EC.presence_of_element_located(self.loc_country))
        from selenium.webdriver.support.ui import Select
        Select(dropdown).select_by_visible_text(country)

    def select_state(self, state):
        dropdown = self.wait.until(EC.presence_of_element_located(self.loc_state))
        from selenium.webdriver.support.ui import Select
        Select(dropdown).select_by_visible_text(state)

    def enter_address(self, address):
        self.wait.until(EC.presence_of_element_located(self.loc_address)).clear()
        self.driver.find_element(*self.loc_address).send_keys(address)
        self.driver.find_element(*self.loc_address1).send_keys('A1')

    def enter_city(self, address):
        self.wait.until(EC.presence_of_element_located(self.loc_address)).clear()
        self.driver.find_element(*self.loc_city).send_keys(address)

    def enter_postal_code(self, code):
        self.wait.until(EC.presence_of_element_located(self.loc_postal_code)).clear()
        self.driver.find_element(*self.loc_postal_code).send_keys(code)

    def click_save(self):
        self.wait.until(EC.element_to_be_clickable(self.loc_save_btn)).click()

    def capture_error_messages(self):
        return self.wait.until(EC.presence_of_element_located(self.loc_error_msg)).text

    def capture_success_message(self):
        return self.wait.until(EC.presence_of_element_located(self.loc_success_msg)).text
