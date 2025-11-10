from selenium import webdriver
from Pages.main_page import MainPage
from selenium.webdriver.chrome.options import Options
import os


def test_navigation_links():
    options = Options()
    if os.getenv("RUN_IN_DOCKER"):
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    options.add_argument("--window-size=1920,1080")

    with webdriver.Chrome(options=options) as driver:
        driver.get("https://effective-mobile.ru/")

        page = MainPage(driver)

        page.click_about()
        page.click_services()
        page.click_projects()
        page.click_reviews()
        page.click_contacts()
