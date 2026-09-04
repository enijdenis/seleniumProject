
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((by, locator))
        ).click()

    def write(self, by, locator, text):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((by, locator))
            ).send_keys(text)

    def get_text(self, by, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((by, locator))
        ).text