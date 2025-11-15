import allure
from Pages.main_page import MainPage


@allure.feature("Навигация по главной странице")
@allure.severity(allure.severity_level.CRITICAL)
def test_navigation_links(driver):
    driver.get("https://effective-mobile.ru/")
    page = MainPage(driver)

    with allure.step("Переход к блоку 'О нас'"):
        page.click(page.about_link)
        assert page.is_visible(page.about_box)
        assert "#about" in driver.current_url

    with allure.step("Переход к блоку 'Услуги'"):
        page.click(page.services_link)
        assert page.is_visible(page.services_box)
        assert "#moreinfo" in driver.current_url

    with allure.step("Переход к блоку 'Проекты'"):
        page.click(page.projects_link)
        assert page.is_visible(page.projects_box)
        assert "#cases" in driver.current_url

    with allure.step("Переход к блоку 'Отзывы'"):
        page.click(page.reviews_link)
        assert page.is_visible(page.reviews_box)
        assert "#Reviews" in driver.current_url

    with allure.step("Переход к блоку 'Контакты'"):
        page.click(page.contacts_link)
        assert page.is_visible(page.contacts_box)
        assert "#contacts" in driver.current_url
