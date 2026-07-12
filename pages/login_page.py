from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class LoginPage:
    """
    Page Object Model (POM) for the SauceDemo login page.

    The idea: this class knows *how to find and interact with* the login
    page's elements. Your test files only call methods like login() or
    is_inventory_page() — they never touch By.ID or CSS selectors directly.
    If SauceDemo changes its HTML, you fix it in ONE place (here), not in
    every test.
    """

    def __init__(self, driver):
        self.driver = driver
        # Locators: (strategy, value) tuples used with find_element(*locator)
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR, "h3[data-test='error']")

    def open(self, url):
        """Navigate the browser to the given URL."""
        self.driver.get(url)

    def enter_username(self, username):
        """Type into the username field."""
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        """Type into the password field."""
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        """Click the login button."""
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        """Convenience method: fills both fields and submits in one call."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        """
        Returns the error text shown after a failed login attempt,
        or None if no error is present (e.g. login succeeded).
        """
        try:
            return self.driver.find_element(*self.error_message).text
        except NoSuchElementException:
            return None

    def is_inventory_page(self):
        """True if login succeeded and we've landed on the products page."""
        return "inventory" in self.driver.current_url
