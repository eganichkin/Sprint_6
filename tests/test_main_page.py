import allure
import pytest
from data import ANSWERS
from pages.main_page import MainPage


class TestMainPage:

    @pytest.mark.parametrize(
        'number, expected_result',
        [
            (0, ANSWERS[1]),
            (1, ANSWERS[2]),
            (2, ANSWERS[3]),
            (3, ANSWERS[4]),
            (4, ANSWERS[5]),
            (5, ANSWERS[6]),
            (6, ANSWERS[7]),
            (7, ANSWERS[8])
        ]
    )
    @allure.title('Проверка текста вопросов в выпадающем списке раздела «Вопросы о важном»')
    @allure.description('На главной странице сайта ищем вопрос под номером {number} и проверяем, что ниже '
                        'представленный ответ на него совпадает с ожидаемым результатом')
    def test_questions_list_select_number_question_check_correct_of_answer(self, driver, number, expected_result):
        main_page = MainPage(driver)
        actual_result = main_page.get_answer_text(number)
        assert expected_result == actual_result
