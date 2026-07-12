import sys
import os

#Allow imports form the project root (config.py, pages/ , utils/)
#when pytest runs form inside the 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
import config
from utils.driver_factory import get_driver
from utils.excel_report import log_result
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    """
    Pytest fixture: runs before each test to create a fresh browser,
    yields it to the test, then quits it afterward (cleanup),
    even if the test fails.
    """
    drv = get_driver()
    yield drv
    drv.quit()


def run_and_log(test_name, test_func):
    """
    Shared wrapper: runs a test function, logs PASS/FAIL/ERROR to Excel,
    and re-raises so pytest still reports it correctly in the terminal.
    """
    try:
        test_func()
        log_result(test_name, "PASS")
    except AssertionError as e:
        log_result(test_name, "FAIL", str(e))
        raise
    except Exception as e:
        log_result(test_name, "ERROR", str(e))
        raise


def test_valid_login(driver):
    """Test Case 1: correct username + password should reach the inventory page."""
    def _run():
        page = LoginPage(driver)
        page.open(config.BASE_URL)
        page.login(config.VALID_USERNAME, config.VALID_PASSWORD)
        assert page.is_inventory_page(), "Did not land on inventory page after valid login"

    run_and_log("Valid Login", _run)


def test_invalid_login(driver):
    """Test Case 2: wrong username + password should show the error message."""
    def _run():
        page = LoginPage(driver)
        page.open(config.BASE_URL)
        page.login(config.INVALID_USERNAME, config.INVALID_PASSWORD)
        error = page.get_error_message()
        assert error is not None and "do not match" in error, \
            f"Expected 'do not match' error, got: {error}"

    run_and_log("Invalid Login", _run)


def test_empty_username(driver):
    """Test case 3: submitting with a blank username should be rejected."""
    def _run():
        page = LoginPage(driver)
        page.open(config.BASE_URL)
        page.login("", config.VALID_PASSWORD)
        error = page.get_error_message()
        assert error is not None and "Username is required" in error, \
            f"Expected username-required error, got: {error}"

    run_and_log("Empty Username", _run)


def test_empty_password(driver):
    """Test case 3: submitting with a blank password should be rejected."""
    def _run():
        page = LoginPage(driver)
        page.open(config.BASE_URL)
        page.login(config.VALID_USERNAME, "")
        error = page.get_error_message()
        assert error is not None and "Password is required" in error, \
            f"Expected password-required error, got: {error}"

    run_and_log("Empty Password", _run)


def test_both_fields_empty(driver):
    """Test case 4: submitting with both fields blank should show an error."""
    def _run():
        page = LoginPage(driver)
        page.open(config.BASE_URL)
        page.login("", "")
        error = page.get_error_message()
        assert error is not None and "Username is required" in error, \
            f"Expected username-required error, got: {error}"

    run_and_log("Both Fields Empty", _run)


def test_locked_out_user(driver):
    """Test Case 5: a locked-out account should be blocked with a specific message."""
    def _run():
        page = LoginPage(driver)
        page.open(config.BASE_URL)
        page.login(config.LOCKED_OUT_USERNAME, config.VALID_PASSWORD)
        error = page.get_error_message()
        assert error is not None and "locked out" in error, \
            f"Expected locked-out error, got: {error}"

    run_and_log("Locked User", _run)
