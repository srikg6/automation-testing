from selenium.webdriver.common.by import By
from utils.helpers import Waits


class BasePage:
    def __init__(self, driver, base_url=None, timeout=10):
        self.driver = driver
        self.base_url = base_url or "https://practice.automationtesting.in"
        self.w = Waits(driver, timeout)


    def open(self, path="/"):
        self.driver.get(self.base_url.rstrip('/') + path)
        return self


    def click(self, locator):
        self.w.clickable(locator).click()


    def type(self, locator, text, clear=True):
        el = self.w.visible(locator)
        if clear:
            el.clear()
            el.send_keys(text)


    def text_of(self, locator):
        return self.w.visible(locator).text.strip()


    def is_present(self, locator):
        try:
            self.w.present(locator)
            return True
        except Exception as ex:
            print(ex)
            return False


    # Common locators
    MENU_SHOP = (By.LINK_TEXT, "Shop")
    MENU_MY_ACCOUNT = (By.LINK_TEXT, "My Account")
    MENU_HOME = (By.LINK_TEXT, "Home")


    def go_shop(self):
        self.click(self.MENU_SHOP)


    def go_my_account(self):
        self.click(self.MENU_MY_ACCOUNT)