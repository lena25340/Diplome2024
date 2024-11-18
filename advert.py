from selenium.webdriver.common.by import By


class Advert:
    def __init__(self, driver):
        self.driver = driver

    def close_advert(self):
        self.driver.find_element(By.CSS_SELECTOR, ".popmechanic-close").click()