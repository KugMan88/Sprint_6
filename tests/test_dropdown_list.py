import pytest
import allure
from locators.main_page_locators import MainPageLocators
from data.main_page_data import FaqAnswersData
from pages.main_page import MainPage

@allure.feature('FAQ на главной странице "Яндекс Самокат"')
class TestFaqHomePage:

    @allure.title('Тест открытия ответов в FAQ')
    @allure.description('Клик по вопросам FAQ по очереди > открываются ответы на вопросы по очереди')
    @pytest.mark.parametrize(
        'button, answer, expected_text',
        [
            [MainPageLocators.cost_question_button, MainPageLocators.cost_answer_text,
             FaqAnswersData.cost_answer],
            [MainPageLocators.several_scooters_question_button, MainPageLocators.several_scooters_answer_text,
             FaqAnswersData.several_scooters_answer],
            [MainPageLocators.rental_time_question_button, MainPageLocators.rental_time_answer_text,
             FaqAnswersData.rental_time_answer],
            [MainPageLocators.today_rent_question_button, MainPageLocators.today_rent_answer_text,
             FaqAnswersData.today_rent_answer],
            [MainPageLocators.question_extend_order_button, MainPageLocators.answer_extend_order_text,
             FaqAnswersData.answer_extend_order],
            [MainPageLocators.charge_question_button, MainPageLocators.charge_answer_text,
             FaqAnswersData.charge_answer],
            [MainPageLocators.question_cancellation_of_order_button, MainPageLocators.answer_cancellation_of_order_text,
             FaqAnswersData.answer_cancellation_of_order],
            [MainPageLocators.mkad_question_button, MainPageLocators.mkad_answer_text,
             FaqAnswersData.mkad_answer]
        ]
    )
    def test_faq_list_click_on_questions_check_answer_(self, driver, button, answer, expected_text):
        main_page = MainPage(driver)
        main_page.click_question_button(button)
        main_page.check_answer_text(answer, expected_text)