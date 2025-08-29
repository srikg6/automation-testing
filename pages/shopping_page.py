import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # === Locators ===
    loc_selenium_link = (By.LINK_TEXT, "selenium")
    loc_add_to_basket_btn = (By.XPATH, "//*[@id='content']/ul/li/a[2]")
    loc_shopping_cart = (By.ID, "wpmenucartli")
    loc_product_name = (By.LINK_TEXT, "Selenium Ruby")
    loc_delete_btn = (By.CSS_SELECTOR, "form > table > tbody > tr.cart_item > td.product-remove > a")
    loc_items_count = (By.XPATH, "//*[@id='wpmenucartli']/a/span[1]")
    # loc_shopping_cart = (By.XPATH, "//a[@title='View your shopping cart']")

    def click_selenium(self):
        self.driver.find_element(*self.loc_selenium_link).click()

    def click_on_add_to_basket(self):
        self.wait.until(EC.presence_of_element_located(self.loc_add_to_basket_btn)).click()

    def click_shopping_cart(self):
        time.sleep(3)
        self.driver.find_element(*self.loc_shopping_cart).click()
        text = self.driver.find_element(self.loc_items_count).text


    def verify_product_in_cart(self, exp):
        time.sleep(10)
        time.sleep(15)
        text = self.wait.until(EC.presence_of_element_located(self.loc_product_name)).text
        if text == exp:
            pass
        else:
            raise "product verification failed"

    def get_book_text(self):
        text = self.driver.find_element(By.TAG_NAME, "h3").text
        return text

    def click_delete_book_from_cart(self):
        var = self.driver.find_element(By.CSS_SELECTOR, self.loc_delete_btn)
        if var.is_displayed():
            var.click()
        else:
            raise
        var1 = self.driver.find_element(By.CSS_SELECTOR, self.loc_delete_btn)
        if var.is_displayed is False:
            pass
        else:
            raise
        if var == var1:
            raise
        else:
            pass


