import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Соглашаемся на сохранение cookies')
    def agree_to_save_cookies(self):
        self.click_to_element_by_script(MainPageLocators.COOKIES_BUTTON)

    @allure.step('Находим и кликаем на элемент с вопросом')
    def click_to_question(self, number):
        question_locator = self.format_locators(MainPageLocators.QUESTION_LOCATOR, number)
        last_question_locator = self.format_locators(MainPageLocators.QUESTION_LOCATOR, 7)

        self.scroll_to_element(last_question_locator)
        self.click_to_element_by_script(question_locator)

    @allure.step('Находим и считываем текст элемента с ответом')
    def get_answer_text(self, number):
        self.open_page(self.url)
        self.agree_to_save_cookies()

        answer_locator = self.format_locators(MainPageLocators.ANSWER_LOCATOR, number)
        self.click_to_question(number)
        return self.get_text_from_element(answer_locator)
