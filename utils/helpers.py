from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Waits:
    OVERLAY = (By.CSS_SELECTOR, ".blockUI.blockOverlay") # WooCommerce/Ajax overlay


    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)


    def visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))


    def clickable(self, locator):
        self.invisible(self.OVERLAY)
        return self.wait.until(EC.element_to_be_clickable(locator))


    def present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))


    def invisible(self, locator):
        try:
            self.wait.until(EC.invisibility_of_element_located(locator))
        except Exception as ex:
            print(ex)
    

    def text_present(self, locator, text):
        return self.wait.until(EC.text_to_be_present_in_element(locator, text))