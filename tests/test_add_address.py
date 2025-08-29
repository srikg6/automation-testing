import logging
import pytest
from pages.billing_address_page import BillingAddressPage
from utils.constants import Constants
from pages.home_page import HomePage
from pages.my_account_page import MyAccountPage

@pytest.mark.positive
def test_update_billing_address(driver):
    """ This test updates the billing address with all the attributes filled"""
    try:
        home = HomePage(driver)
        my_account = MyAccountPage(driver)
        # 1) Open the browser and enter the URL
        driver.get(Constants.URL)
        logging.info("Successfully launched the url")
        home.click_my_account()
        my_account.login("nanizinda@gmail.com", "Nani@143143")
        # home.click_my_account()
        home.click_addresses()
        logging.info("Clicked on Addresses link successfully")
        driver.implicitly_wait(3)
        my_account.edit_billing_address()
        billing_page = BillingAddressPage(driver)
        billing_page.enter_first_name("Srikanth")
        logging.info("Successfully entered first name")
        billing_page.enter_last_name("Gattupalli")
        logging.info("Successfully entered last name")
        # billing_page.enter_email("nanizinda@gmail.com")
        billing_page.enter_phone("8904833828")
        logging.info("Successfully entered mobile number")
        billing_page.select_country("India")
        logging.info("Successfully entered country")
        billing_page.enter_address("Ameenpur")
        logging.info("Successfully entered address")
        billing_page.enter_city("Hyderabad")
        logging.info("Successfully entered city name")
        # commented the below just to expedite my work and close it
        # We can do by switching to the iframe
        # billing_page.select_state("Telangana")
        # logging.info("Successfully entered state name")
        billing_page.enter_postal_code(502032)
        logging.info("Successfully entered postal code")
        billing_page.click_save()
        logging.info("Successfully clicked on save button")
        msg = billing_page.capture_success_message()
        assert msg == "Address changed successfully.",\
            "Error message displayed doesn't match with the expected"
        logging.info("Successfully verified the success message")
    except Exception as ex:
        logging.error(f"An exception occured: {ex}")
        raise

@pytest.mark.negative
def test_update_billing_address_with_mandatory_attribute_skipped(driver):
    """ This test captures the error msg for the mandatory attribute - First Name """
    try:
        home = HomePage(driver)
        my_account = MyAccountPage(driver)
        # 1) Open the browser and enter the URL
        driver.get(Constants.URL)
        logging.info("Successfully launched the url")
        home.click_my_account()
        my_account.login("nanizinda@gmail.com", "Nani@143143")
        # home.click_my_account()
        home.click_addresses()
        logging.info("Clicked on Addresses link successfully")
        driver.implicitly_wait(3)
        my_account.edit_billing_address()
        billing_page = BillingAddressPage(driver)
        billing_page.enter_first_name("")
        logging.info("Successfully entered first name")
        billing_page.enter_last_name("Gattupalli")
        logging.info("Successfully entered last name")
        # billing_page.enter_email("nanizinda@gmail.com")
        billing_page.enter_phone("8904833828")
        logging.info("Successfully entered mobile number")
        billing_page.select_country("India")
        logging.info("Successfully entered country")
        billing_page.enter_address("Ameenpur")
        logging.info("Successfully entered address")
        billing_page.enter_city("Hyderabad")
        logging.info("Successfully entered city name")
        # commented the below just to expedite my work and close it
        # We can do by switching to the iframe
        # billing_page.select_state("Telangana")
        # logging.info("Successfully entered state name")
        billing_page.enter_postal_code(502032)
        logging.info("Successfully entered postal code")
        billing_page.click_save()
        error = billing_page.capture_error_messages()
        assert error == "First Name is a required field.",\
            "Error message displayed doesn't match with the expected"
    except Exception as ex:
        logging.error(f"An exception occured: {ex}")
        raise


