import logging
import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.constants import Constants
from pages.home_page import HomePage
from pages.my_account_page import MyAccountPage


@pytest.mark.positive
def test_registration_sign_in_with_valid_email_password(driver):
    """ This test verifies whether the user is able to login
        with valid email and valid password """
    try:
        home = HomePage(driver)
        my_account = MyAccountPage(driver)
        # 1) Open the browser and enter the URL
        driver.get(Constants.URL)
        # page.open(driver, Constants.URL)
        logging.info("Successfully launched the url")
        home.click_my_account()
        logging.info("Clicked on my account link successfully")
        # 3) Enter Email Address
        my_account.enter_email("testuser12345_13@example.com")
        logging.info("Entered the email successfully")
        # 4) Enter Password
        my_account.enter_password(Constants.PASSWORD)
        logging.info("Entered the password successfully")
        # 5) Click on Register button
        my_account.click_register_button(True)
        logging.info("Successfully clicked on the Register button")
        # 6) Wait until navigation / logout link appears
        ele = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(my_account.loc_logout_link)
        )
        # 7) Assert successful registration
        assert ele.is_displayed() is True, \
            "Login with valid email and password is not successful"
        logging.info("Successfully verified the logout link")
    except Exception as ex:
        logging.error(f"An error occurred in "
                          f"{test_registration_sign_in_with_valid_email_password.__name__} function: \n%s", ex)
        raise

@pytest.mark.negative
def test_registration_with_invalid_email_valid_password(driver):
    """ This test verifies whether the user is able to login
        with invalid email and valid password """
    try:
        home = HomePage(driver)
        my_account = MyAccountPage(driver)
        # 1) Open the browser and enter the URL
        driver.get(Constants.URL)
        # page.open(driver, Constants.URL)
        logging.info("Successfully launched the url")
        home.click_my_account()
        logging.info("Clicked on my account link successfully")
        # 3) Enter Email Address
        my_account.enter_email(Constants.INV_EMAIL_ID)
        logging.info("Entered the email successfully")
        # 4) Enter Password
        my_account.enter_password(Constants.PASSWORD)
        logging.info("Entered the password successfully")
        # 5) Click on Register button
        my_account.click_register_button(True)
        logging.info("Successfully clicked on the Register button")
        # 7) Get error message
        time.sleep(10)
        my_account.capture_error_and_validate(Constants.INV_EMAIL_ERROR_MSG)
    except Exception as ex:
        logging.error(f"An error occurred in "
                          f"{test_registration_with_invalid_email_valid_password.__name__} function: \n%s", ex)
        raise

@pytest.mark.negative
def test_registration_with_valid_email_invalid_password(driver):
    """ This test verifies whether the user is able to login
        with valid email and invalid password """
    try:
        home = HomePage(driver)
        my_account = MyAccountPage(driver)
        # 1) Open the browser and enter the URL
        driver.get(Constants.URL)
        # page.open(driver, Constants.URL)
        logging.info("Successfully launched the url")
        home.click_my_account()
        logging.info("Clicked on my account link successfully")
        # 3) Enter Email Address
        my_account.enter_email(Constants.EMAIL)
        logging.info("Entered the email successfully")
        # 4) Enter Password
        my_account.enter_password(Constants.INV_PASSWORD)
        logging.info("Entered the password successfully")
        # 5) Click on Register button
        my_account.click_register_button(False)
        logging.info("Successfully clicked on the Register button")
    except Exception as ex:
        logging.error(f"An error occurred in "
                          f"{test_registration_with_valid_email_invalid_password.__name__} function: \n%s", ex)
        raise

@pytest.mark.negative
def test_registration_with_blank_email_and_password(driver):
    """ This test verifies whether the user is able to login
        with blank email and blank password """
    try:
        home = HomePage(driver)
        my_account = MyAccountPage(driver)
        # 1) Open the browser and enter the URL
        driver.get(Constants.URL)
        logging.info("Successfully launched the url")
        home.click_my_account()
        logging.info("Clicked on my account link successfully")
        # 3) Enter Email Address
        my_account.enter_email(Constants.BLANK_EMAIL)
        logging.info("Entered the email successfully")
        # 4) Enter Password
        my_account.enter_password(Constants.BLANK_PASSWORD)
        logging.info("Entered the password successfully")
        # 5) Click on Register button
        my_account.click_register_button(True)
    except Exception as ex:
        logging.error(f"An error occurred in "
                          f"{test_registration_with_blank_email_and_password.__name__} function: \n%s", ex)
        raise

@pytest.mark.negative
def test_registration_with_invalid_email_and_password(driver):
    try:
        home = HomePage(driver)
        my_account = MyAccountPage(driver)
        # 1) Open the browser and enter the URL
        driver.get(Constants.URL)
        # page.open(driver, Constants.URL)
        logging.info("Successfully launched the url")
        home.click_my_account()
        logging.info("Clicked on my account link successfully")
        # 3) Enter Email Address
        my_account.enter_email(Constants.INV_EMAIL_ID)
        logging.info("Entered the email successfully")
        # 4) Enter Password
        my_account.enter_password(Constants.INV_PASSWORD)
        logging.info("Entered the password successfully")
        # 5) Verify whether the Registration button is disabled
        my_account.click_register_button(False)
        logging.info("Register button is in disabled mode")
    except Exception as ex:
        logging.error(f"An error occurred in "
                          f"{test_registration_with_invalid_email_and_password.__name__} function: \n%s", ex)
        raise

@pytest.mark.positive
def test_login_with_valid_email_password(driver):
    """ This test verifies whether the user is able to login
        with valid username and valid password """
    try:
        home = HomePage(driver)
        my_account = MyAccountPage(driver)
        # 1) Open the browser and enter the URL
        driver.get(Constants.URL)
        # page.open(driver, Constants.URL)
        logging.info("Successfully launched the url")
        home.click_my_account()
        logging.info("Clicked on my account link successfully")
        # 3) Enter Email Address
        res = my_account.login(Constants.EMAIL, Constants.PASSWORD)
        if res is False:
            logging.error(f"Failed to login to the application")
        else:
            logging.info("Successfully entered the credentials and logged in")

        # 6) Wait until navigation / logout link appears
        ele = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(my_account.is_logout_link_displayed())
        )
        # 7) Assert successful registration
        assert ele.is_displayed() is True, \
            "Login with valid email and password is not successful"
        logging.info("Successfully verified the logout link")
    except Exception as ex:
        logging.error(f"An error occurred in "
                          f"{test_login_with_valid_email_password.__name__} function: \n%s", ex)
        raise

@pytest.mark.negative
def test_login_with_invalid_email_valid_password(driver):
    """ This test verifies whether the user is able to login
        with invalid username and valid password """
    try:
        home = HomePage(driver)
        my_account = MyAccountPage(driver)
        # 1) Open the browser and enter the URL
        driver.get(Constants.URL)
        # page.open(driver, Constants.URL)
        logging.info("Successfully launched the url")
        home.click_my_account()
        logging.info("Clicked on my account link successfully")
        # 3) Enter Email Address
        res = my_account.login(Constants.INV_EMAIL_ID, Constants.PASSWORD)
        if res is False:
            logging.error(f"Failed to login to the application")
        else:
            logging.info("Successfully entered the credentials and logged in")
        my_account.capture_error_and_validate(Constants.INV_EMAIL_LOGIN_ERROR_MSG)
        logging.info("Successfully verified the displayed")
    except Exception as ex:
        logging.error(f"An error occurred in "
                          f"{test_login_with_invalid_email_valid_password.__name__} function: \n%s", ex)
        raise

@pytest.mark.negative
def test_login_with_valid_email_invalid_password(driver):
    """This test verifies whether the user is able to login
        with valid username and invalid password """
    try:
        home = HomePage(driver)
        my_account = MyAccountPage(driver)
        # 1) Open the browser and enter the URL
        driver.get(Constants.URL)
        # page.open(driver, Constants.URL)
        logging.info("Successfully launched the url")
        home.click_my_account()
        logging.info("Clicked on my account link successfully")
        # 3) Enter Email Address
        res = my_account.login(Constants.EMAIL, Constants.INV_PASSWORD)
        if res is False:
            logging.error(f"Failed to login to the application")
        else:
            logging.info("Successfully entered the credentials and logged in")
        my_account.capture_error_and_validate(Constants.INV_PASSWORD_LOGIN_ERROR_MSG)
        logging.info("Successfully verified the error message displayed")
    except Exception as ex:
        logging.error(f"An error occurred in "
                          f"{test_login_with_valid_email_invalid_password.__name__} function: \n%s", ex)
        raise

@pytest.mark.negative
def test_login_with_blank_email_blank_password(driver):
    """This test verifies whether the user is able to login
    with blank username and password """
    try:
        home = HomePage(driver)
        my_account = MyAccountPage(driver)
        # 1) Open the browser and enter the URL
        driver.get(Constants.URL)
        # page.open(driver, Constants.URL)
        logging.info("Successfully launched the url")
        home.click_my_account()
        logging.info("Clicked on my account link successfully")
        # 3) Enter Email Address
        res = my_account.login(Constants.BLANK_EMAIL, Constants.BLANK_PASSWORD)
        if res is False:
            logging.error(f"Failed to login to the application")
        else:
            logging.info("Successfully entered the credentials and logged in")
        my_account.capture_error_and_validate(Constants.LOGIN_BLANK_USERNAME_PASSWORD)
        logging.info("Successfully verified the error message displayed")
    except Exception as ex:
        logging.error(f"An error occurred in "
                          f"{test_login_with_blank_email_blank_password.__name__} function: \n%s", ex)
        raise

@pytest.mark.negative
def test_login_with_invalid_email_invalid_password(driver):
    """This test verifies whether the user is able to login
        with invalid email and invalid password """
    try:
        home = HomePage(driver)
        my_account = MyAccountPage(driver)
        # 1) Open the browser and enter the URL
        driver.get(Constants.URL)
        # page.open(driver, Constants.URL)
        logging.info("Successfully launched the url")
        home.click_my_account()
        logging.info("Clicked on my account link successfully")
        # 3) Enter Email Address
        res = my_account.login(Constants.INV_EMAIL_ID, Constants.INV_PASSWORD)
        if res is False:
            logging.error(f"Failed to login to the application")
        else:
            logging.info("Successfully entered the credentials and logged in")
        my_account.capture_error_and_validate(Constants.LOGIN_BLANK_USERNAME_PASSWORD)
        logging.info("Successfully verified the error message displayed")
    except Exception as ex:
        logging.error(f"An error occurred in "
                      f"{test_login_with_blank_email_blank_password.__name__} function: \n%s", ex)
        raise
