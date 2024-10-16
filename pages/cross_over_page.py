import allure
from pages.base_page import BasePage
from locators.cross_over_locators import CrossOverLocators


class CrossOverPage(BasePage):

    @allure.step('Находим и кликаем на логотим "Яндекс"')
    def click_to_yandex_logo(self):
        self.click_to_element(CrossOverLocators.YANDEX_LOGO_LOCATOR)

    @allure.step('Находим и кликаем на логотим "Самокат"')
    def click_to_scooter_logo(self):
        self.click_to_element(CrossOverLocators.SCOOTER_LOGO_LOCATOR)

    @allure.step('Перехоим на страницу оформления заказа')
    def open_order_page(self):
        self.open_page(self.url + 'order')

    @allure.step('Переходим на основную страницу сайта "Самокат"')
    def open_main_page(self):
        self.open_page(self.url)

    def cross_over_from_yandex_logo_hyperlink(self, expected_url):
        self.open_main_page()
        self.click_to_yandex_logo()

        self.wait_for_redirect(expected_url)
        return self.current_url()

    def cross_over_from_scooter_logo_hyperlink(self):
        self.open_order_page()
        self.click_to_scooter_logo()
        return self.current_url()
