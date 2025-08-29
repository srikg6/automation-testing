import time
import logging
import pytest
from utils.constants import Constants
from pages.home_page import HomePage
from pages.my_account_page import MyAccountPage
from pages.shopping_page import ShopPage

@pytest.mark.positive
def test_add_products_to_cart(driver):
    """ This test updates the billing address with all the attributes filled
    It adds selenium Ruby product to the cart and verifies if it's to the cart """
    try:
        home = HomePage(driver)
        my_account = MyAccountPage(driver)
        shop_page = ShopPage(driver)
        # 1) Open the browser and enter the URL
        driver.get(Constants.URL)
        logging.info("Successfully launched the url")
        home.click_shop()
        shop_page.click_selenium()
        text = shop_page.get_book_text()
        time.sleep(3)
        shop_page.click_on_add_to_basket()
        logging.info("Successfully added the book")
        # Verify whether it is added to the cart
        shop_page.click_shopping_cart()
        shop_page.verify_product_in_cart(text)
        logging.info("Product verification successful")
    except Exception as ex:
        logging.error(f"An exception occured: {ex}")
        raise

@pytest.mark.positive
def test_delete_products_from_cart(driver):
    """ This test deletes the product from the cart """
    try:
        home = HomePage(driver)
        my_account = MyAccountPage(driver)
        shop_page = ShopPage(driver)
        # 1) Open the browser and enter the URL
        driver.get(Constants.URL)
        logging.info("Successfully launched the url")
        home.click_shop()
        # shop_page.click_selenium()
        # text = shop_page.get_book_text()
        # time.sleep(3)
        # shop_page.click_on_add_to_basket()
        # logging.info("Successfully added the book")
        # Verify whether it is added to the cart
        shop_page.click_shopping_cart()
        shop_page.click_delete_book_from_cart()
    except Exception as ex:
        logging.error(f"An exception occured: {ex}")
        raise