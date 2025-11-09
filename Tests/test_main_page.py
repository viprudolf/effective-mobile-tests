from selenium import webdriver
from Pages.main_page import MainPage
import time


def test_navigation_links():
    with webdriver.Chrome() as driver:
        driver.maximize_window()
        driver.get("https://effective-mobile.ru/")

        page = MainPage(driver)

        page.click_about()
        page.click_services()
        page.click_projects()
        page.click_reviews()
        page.click_contacts()

