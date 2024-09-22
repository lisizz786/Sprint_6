import pytest
import allure
from pages.home_page import ScooterHomePage
from src.data import ScooterHomePageFAQ
from src.locators import ScooterHomePageLocator


@allure.epic('Upgrade Main page')
@allure.parent_suite('Домашняя страница')
@allure.suite('Suite_FAQ')
class TestScooterFAQPage:
    @allure.feature('Вопрос/ответ на Домашней страницы')
    @allure.story('Раскрытие ответа')
    @allure.title('При нажатии на вопрос раскрывается ответ')
    @allure.description('Соответствие текста')
    @pytest.mark.parametrize(
        "question,answer,expected_answer",
        [
            (0, 0, ScooterHomePageFAQ.answer1),
            (1, 1, ScooterHomePageFAQ.answer2),
            (2, 2, ScooterHomePageFAQ.answer3),
            (3, 3, ScooterHomePageFAQ.answer4),
            (4, 4, ScooterHomePageFAQ.answer5),
            (5, 5, ScooterHomePageFAQ.answer6),
            (6, 6, ScooterHomePageFAQ.answer7),
            (7, 7, ScooterHomePageFAQ.answer8),
        ]
    )
    def test_faq_click_first_question_show_answer(self, driver, question, answer, expected_answer):
        scooter_home_page = ScooterHomePage(driver)
        scooter_home_page.go_to_site()
        scooter_home_page.click_cookie_accept()
        scooter_home_page.click_faq_question(question_number=question)
        answer = scooter_home_page.find_element(ScooterHomePageLocator.FAQ_ANSWER(answer_number=answer))

        assert answer.is_displayed() and answer.text == expected_answer