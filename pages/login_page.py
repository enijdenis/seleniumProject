from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage

class LoginPage(BasePage):

    def login(self, username, password):
        self.write(By.ID, "username", username)
        self.write(By.ID,"password", password )
        self.click(By.CSS_SELECTOR, ".radius")

    def get_login_message(self):
        return self.get_text(By.ID, "flash")

