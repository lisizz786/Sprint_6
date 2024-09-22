import pytest
import allure
from pages.home_page import ScooterHomePage
from src.urls import Urls
from src.locators import ScooterHomePageLocator


@allure.epic('Main page')
@allure.parent_suite('Домашняя страница')
@allure.suite('Suite_Header')
class TestScooterHomePage:

    @allure.feature('Оформление заказа из Домашней страницы')
    @allure.story('Оформление заказа по кнопке "Заказать" из header')
    @allure.title('Нажатие на кнопку "Заказать" в header')
    @allure.description('Корректный переход на страницу Оформление заказа')
    def test_click_top_order_button_show_order_page(self, driver):
        scooter_home_page = ScooterHomePage(driver)
        scooter_home_page.go_to_site()
        scooter_home_page.click_cookie_accept()
        scooter_home_page.click_top_order_button()
        assert scooter_home_page.current_url() == Urls.ORDER_PAGE

    @allure.feature('Оформление заказа из Домашней страницы')
    @allure.story('Оформление заказа по кнопке "Заказать" из блока "Как это работает"')
    @allure.title('Заказать в блоке "Как это работает"')
    @allure.description('Переход на страницу "Оформления заказа"')
    def test_click_bottom_order_button_show_order_page(self, driver):
        scooter_home_page = ScooterHomePage(driver)
        scooter_home_page.go_to_site()
        scooter_home_page.click_cookie_accept()
        scooter_home_page.click_bottom_order_button()

        assert scooter_home_page.current_url() == Urls.ORDER_PAGE

    @allure.feature('Переход на страницу "ЯндексДзен" из Домашней страницы')
    @allure.story('Редирект на страницу ЯндексДзен по кнопке logo в header')
    @allure.title('При нажатии на лого "Яндекс" происходит редирект на страницу "ЯндексДзен"')
    @allure.description('Корректный редирект на страницу "ЯндексДзен"')
    def test_click_yandex_button_go_to_yandex(self, driver):
        scooter_home_page = ScooterHomePage(driver)
        scooter_home_page.go_to_site()
        scooter_home_page.click_cookie_accept()
        scooter_home_page.click_yandex_button()
        scooter_home_page.switch_window(1)
        scooter_home_page.wait_url_until_not_about_blank()
        current_url = scooter_home_page.current_url()

        assert (Urls.YANDEX_HOME_PAGE in current_url) or (Urls.DZEN_HOME_PAGE in current_url) or (Urls.YANDEX_CAPTCHA_PAGE in current_url)

    @allure.feature('Главная страница')
    @allure.story('Редирект по логотипу "Самоката"')
    @allure.title('При нажатии на логотип "Самоката" происходит редирект на главную страницу')
    @allure.description('Проверка что при нажатии на логотип "Самоката" происходит корректный редирект на главную страницу.')
    def test_logo_redirect(self, driver):
        scooter_home_page = ScooterHomePage(driver)
        scooter_home_page.go_to_site()
        scooter_home_page.click_cookie_accept()
        logo_element = scooter_home_page.find_element(ScooterHomePageLocator.SCOOTER_LOGO)
        logo_element.click()
        current_url = scooter_home_page.current_url()

        assert current_url == Urls.MAIN_PAGE, f'Expected URL to be {Urls.MAIN_PAGE}, but got {current_url}'
