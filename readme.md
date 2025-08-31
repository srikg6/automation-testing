# Testcases automated
- verify whether user is able to register with valid email and password.
- verify whether the user is able to register with blank email and blank password.
- verify whether the user is able to register with invalid email and valid password.
- verify whether the user is able to register with valid email and invalid password.
- verify whether the user is able to register with invalid email and invalid password.
- verify whether the user is able to login successfully with valid credentials
- verify whether the user is able to login with invalid email and valid password
- verify whether the user is able to login with valid email and invalid password
- verify whether the user is able to login with blank email and password
- verify whether the user is able to login with invalid email and password
- verify whether the user is able to save the billing address without entering all the mandatory fields
- verify whether the user is able to save the billing address after entering all the mandatory fields
- verify whether the billing address details saved are being reflected same
- verify whether the user is able to save the shipping address without entering all the mandatory fields
- verify whether the user is able to save the shipping address after entering all the mandatory fields
- verify whether the shipping address details saved are being reflected same

# Clubbed both the below tests in a single test
- verify whether the user is able to add the products to the cart from the shopping page
- verify whether the user is able to delete the products from the cart

# Tests that are not automated
- verify the address details are updated properly

# *** Commands to be executed for running the testcase ****
Note: move to the directory under which the tests are present inorder to execute the tests present under the directory and its subdirectories

- pytest -v --html=reports/report.html --self-contained-html
    This commands executes all the tests and html report gets generated under /reports folder.

- pytest -v -m positive --html=reports/report.html --self-contained-html
    This commands executes all the positive tests and html report gets generated under /reports folder.
    If we need to execute only negative tests, replace the marker "positive" with "negative"

- pytest -v
This command executes all the tests from the local repository directory without generating a report.

If the user wants to run one particular testsuite with markers, the below command needs to be executed
pytest -v -m positive tests/test_registration_sign_in.py --html=reports/report.html --self-contained-html

If the user wants to run all tests under a testsuite, the below command needs to be executed
- pytest -v tests/test_registration_sign_in.py --html=reports/report.html --self-contained-html


# Note
modify email - "testuser12345_13@example.com" in test_registration_sign_in.py file to register a new account
else it will fail.
