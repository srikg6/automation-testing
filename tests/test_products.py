import time
import logging
import pytest
from utils.constants import Constants
from pages.home_page import HomePage
# from pages.my_account_page import MyAccountPage
from pages.shopping_page import ShopPage

@pytest.mark.positive
def test_add_products_to_cart(driver):
    """ This test updates the billing address with all the attributes filled
    It adds selenium Ruby product to the cart and verifies if it's to the cart """
    try:
        home = HomePage(driver)
        shop_page = ShopPage(driver)
        # 1) Open the browser and enter the URL
        driver.get(Constants.URL)
        logging.info("Successfully launched the url")
        home.click_shop()
        logging.info("Successfully clicked on shop tab")
        shop_page.click_selenium()
        logging.info("Successfully clicked on selenium link")
        text = shop_page.get_book_text()
        shop_page.click_on_add_to_basket()
        logging.info("Successfully added the book to the cart")
        # Verify whether it is added to the cart
        shop_page.click_shopping_cart(text)
        logging.info("Successfully clicked on the cart and verified the book")
        shop_page.remove_item_from_cart()
        logging.info("Successfully removed the item from the cart")
    except Exception as ex:
        logging.error(f"An exception occured: {ex}")
        raise
