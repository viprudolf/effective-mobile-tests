import time
import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class MainPage:
    about_link = (By.CSS_SELECTOR, "a[href='#about']")
    services_link = (By.CSS_SELECTOR, "a[href='#moreinfo']")
    projects_link = (By.CSS_SELECTOR, "a[href='#cases']")
    reviews_link = (By.CSS_SELECTOR, "a[href='#Reviews']")
    contacts_link = (By.CSS_SELECTOR, "a[href='#contacts']")

    about_box = (By.CSS_SELECTOR, "div.tn-atom[field='tn_text_1680508197707']")
    services_box = (By.CSS_SELECTOR, "div.tn-atom[field='tn_text_1680510339488']")
    projects_box = (By.CSS_SELECTOR, "[data-slide-index='1']")
    reviews_box = (By.CSS_SELECTOR,
                   "#recorddiv699930013 > div.t-slds > div > div > div > div > div.t730__topsection > div > div > strong")
    contacts_box = (By.CSS_SELECTOR, "div.tn-atom[field='tn_text_1680516225306']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def is_visible(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return True
