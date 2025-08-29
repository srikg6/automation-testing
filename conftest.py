import pytest
import logging
import os
from selenium import webdriver

# Create logs directory
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "test_run.log")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="w"),  # write to file
        logging.StreamHandler()                   # also print to console
    ]
)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="function")
def driver():
    """Fixture to initialize and quit the WebDriver for each test"""
    logger.info("Launching browser...")
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    logger.info("Quitting browser...")
    driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logstart(nodeid, location):
    """Logs when a test starts"""
    logger.info(f"===== Test Started: {nodeid} =====")


@pytest.hookimpl(trylast=True)
def pytest_runtest_logreport(report):
    """Logs when a test is executed successfully or failed"""
    if report.when == "call":  # only after test call (not setup/teardown)
        if report.failed:
            logger.error(f"❌ Test Failed: {report.nodeid}")
        elif report.passed:
            logger.info(f"✅ Test Passed: {report.nodeid}")
        elif report.skipped:
            logger.warning(f"⚠️ Test Skipped: {report.nodeid}")
