import pytest
from selenium import webdriver
import os
from dotenv import load_dotenv

load_dotenv()

PASSWORD = os.getenv("PASSWORD")
USER = os.getenv("USER")

@pytest.fixture
def driver():
    # Configuration Firefox en mode headless test sans lancer le navigateur
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")

    driver = webdriver.Firefox(options=options)
    driver.set_window_size(1040, 800)

    #le driver donne la main au test
    yield driver

    driver.quit()