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

    def is_check_object_the_location(self, locator):
        elem = self.wait.until(EC.presence_of_element_located(locator))
        if elem.is_enabled():
            print(f"Элемент найден и доступен'")
            return True
        else:
            print(f"Элемент найден, но недоступен'")
            return False

    def click_link(self, locator):
        elem = self.wait.until(EC.presence_of_element_located(locator))

        self.is_check_object_the_location(locator)

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", elem)
        print(f"Ссылка найдена: {locator} ")

        self.driver.execute_script("arguments[0].click();", elem)
        print(f"Клик по ссылке: {locator}")
        time.sleep(2)

    def check_box(self, locator):
        boxes = self.wait.until(EC.presence_of_all_elements_located(locator))
        for box in boxes:
            if box.is_enabled():
                print(f"Блок найден и видим: {box.text}")

    @allure.feature("Main Page")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Проверка клика на ссылку 'О нас'")
    def click_about(self):
        with allure.step("Открываем страницу и кликаем по ссылке 'О нас'"):
            self.click_link(self.about_link)
        with allure.step("Проверяем перевело ли нас к блоку 'О нас'"):
            self.check_box(self.about_box)
        assert "#about" in self.driver.current_url, "Ссылка 'О нас' не прокрутила страницу к блоку"

    @allure.feature("Main Page")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Проверка клика на ссылку 'Услуги'")
    def click_services(self):
        with allure.step("Открываем страницу и кликаем по ссылке 'Услуги'"):
            self.click_link(self.services_link)
        with allure.step("Проверяем перевело ли нас к блоку 'Услуги'"):
            self.check_box(self.services_box)
        assert "#moreinfo" in self.driver.current_url, "Ссылка 'Услуги' не прокрутила страницу к блоку"

    @allure.feature("Main Page")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Проверка клика на ссылку 'Проекты'")
    def click_projects(self):
        with allure.step("Открываем страницу и кликаем по ссылке 'Проекты'"):
            self.click_link(self.projects_link)
        with allure.step("Проверяем перевело ли нас к блоку 'Проекты'"):
            self.check_box(self.projects_box)
        assert "#cases" in self.driver.current_url, "Ссылка 'Проекты' не прокрутила страницу к блоку"

    @allure.feature("Main Page")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Проверка клика на ссылку 'Отзыв'")
    def click_reviews(self):
        with allure.step("Открываем страницу и кликаем по ссылке 'Отзыв'"):
            self.click_link(self.reviews_link)
        with allure.step("Проверяем перевело ли нас к блоку 'Отзыв'"):
            self.check_box(self.reviews_box)
        assert "#Reviews" in self.driver.current_url, "Ссылка 'Отзывы' не прокрутила страницу к блоку"

    @allure.feature("Main Page")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Проверка клика на ссылку 'Контакты'")
    def click_contacts(self):
        with allure.step("Открываем страницу и кликаем по ссылке 'Контакты'"):
            self.click_link(self.contacts_link)
        with allure.step("Проверяем перевело ли нас к блоку 'Контакты'"):
            self.check_box(self.contacts_box)
        assert "#contacts" in self.driver.current_url, "Ссылка 'Контакты' не прокрутила страницу к блоку"

