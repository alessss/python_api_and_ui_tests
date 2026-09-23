from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import config


class BasePage:
    #All waits are explicit

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.EXPLICIT_WAIT_SECONDS)

    def find_visible(self, by: str, value: str):
        return self.wait.until(EC.visibility_of_element_located((by, value)))

    def find_clickable(self, by: str, value: str):
        return self.wait.until(EC.element_to_be_clickable((by, value)))

    def find_all_present(self, by: str, value: str):
        return self.wait.until(EC.presence_of_all_elements_located((by, value)))

    def click(self, by: str, value: str):
        self.find_clickable(by, value).click()

    def get_text(self, by: str, value: str) -> str:
        return self.find_visible(by, value).text
