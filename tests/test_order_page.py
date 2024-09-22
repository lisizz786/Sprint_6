import pytest
import allure
from src.urls import Urls
from pages.home_page import ScooterHomePage
from pages.order_page import ScooterOrderPage
from src.locators import ScooterOrderPageLocator
from src.data import ScooterOrderPageData as order_data


@allure.epic('Создание заказа')
@allure.parent_suite('Создание заказа')
class TestScooterOrderPage:
    @allure.suite('Заполнение данных на странице "Для кого самокат"')
    @allure.feature('Заполнения данных пользователя в разделе "Для кого самокат"')
    @allure.story('Корректный ввод данных пользователя в разделе "Для кого самокат"')
    @allure.title('Переход в раздел "Про аренду"')
    @allure.description('Переход на следующий этап "Про аренду"')
    def test_order_page_go_to_choose_scooter_user_data_correct_open_about_rent(self, driver):
        scooter_order_page = ScooterOrderPage(driver)
        scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        scooter_home_page = ScooterHomePage(driver)
        scooter_home_page.click_cookie_accept()
        scooter_order_page.fill_user_data(order_data.data_sets['data_set1'])
        scooter_order_page.go_next()
        assert len(scooter_order_page.find_elements(ScooterOrderPageLocator.ORDER_BUTTON)) > 0

    @allure.suite('Заполнение данных на странице "Про аренду"')
    @allure.feature('Заполнения данных пользователя в разделе "Про аренду"')
    @allure.story('Корректный ввод данных пользователя в разделе "Про аренду"')
    @allure.title('Оформление заказа')
    @allure.description('Подтверждение об успешном создании заказа и присвоенным номером')
    @pytest.mark.parametrize('data_set', ['data_set1', 'data_set2'])
    def test_order_page_about_rent_input_correct_data_and_order_show_order_number(self, driver, data_set):
        scooter_order_page = ScooterOrderPage(driver)
        scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        scooter_home_page = ScooterHomePage(driver)
        scooter_home_page.click_cookie_accept()
        scooter_order_page.fill_user_data(order_data.data_sets[data_set])
        scooter_order_page.go_next()
        scooter_order_page.fill_rent_data(order_data.data_sets[data_set])
        scooter_order_page.click_order()
        scooter_order_page.click_accept_order()
        assert len(scooter_order_page.find_elements(ScooterOrderPageLocator.ORDER_COMPLETED_INFO)) > 0

    @allure.suite('Создание заказа')
    @allure.feature('Создание заказа')
    @allure.story('Оформление заказа')
    @allure.title('Переход на страницу с заказом')
    @allure.description('Отображение страницы "Статус заказа" ')
    @pytest.mark.parametrize('data_set', ['data_set1', 'data_set2'])
    def test_order_page_create_order_and_go_order_status(self, driver, data_set):
        scooter_order_page = ScooterOrderPage(driver)
        scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        scooter_home_page = ScooterHomePage(driver)
        scooter_home_page.click_cookie_accept()
        scooter_order_page.fill_user_data(order_data.data_sets[data_set])
        scooter_order_page.go_next()
        scooter_order_page.fill_rent_data(order_data.data_sets[data_set])
        scooter_order_page.click_order()
        scooter_order_page.click_accept_order()
        order_number = scooter_order_page.get_order_number()
        scooter_order_page.click_go_to_status()
        current_url = scooter_order_page.current_url()
        assert (Urls.ORDER_STATUS_PAGE in current_url) and (order_number in current_url)