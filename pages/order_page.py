import allure

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from data import ORDER_INFO
from selenium.webdriver.common.keys import Keys


class OrderPage(BasePage):

    @allure.step('Переходим на форму заполнения информации по аренде нажатием на кнопку "Далее"')
    def cross_over_to_fill_rent_window(self):
        self.click_to_element(OrderPageLocators.NEXT_ORDER_BUTTON)

    @allure.step('Заполняем информацию по клиенту')
    def fill_client_info(self):
        self.send_text_to_element(OrderPageLocators.NAME_INPUT, ORDER_INFO['name'])
        self.send_text_to_element(OrderPageLocators.SURNAME_INPUT, ORDER_INFO['surname'])
        self.send_text_to_element(OrderPageLocators.ADDRESS_INPUT, ORDER_INFO['address'])
        self.send_text_to_element(OrderPageLocators.METRO_INPUT, ORDER_INFO['metro'])
        self.click_to_element(OrderPageLocators.METRO_STATION_SELECT)
        self.send_text_to_element(OrderPageLocators.TELEPHONE_INPUT, ORDER_INFO['telephone'])
        self.cross_over_to_fill_rent_window()

    @allure.step('Заполняем информацию по аренде, сроку доставки и дополнительной информации')
    def fill_rent_info(self):
        self.click_to_element(OrderPageLocators.DATE_DELIVER_INPUT)
        self.send_text_to_element(OrderPageLocators.DATE_DELIVER_INPUT, Keys.ENTER)
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD_INPUT)
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD_SELECT)
        self.click_to_element(OrderPageLocators.SCOOTER_CHECKBOX)
        self.send_text_to_element(OrderPageLocators.COMMENT_INBOX, ORDER_INFO['comment'])

    @allure.step('Завершаем и подтверждаем заказ нажатием на кнопку "Заказать" и "Да"')
    def complete_order(self):
        self.click_to_element(OrderPageLocators.COMPLETE_ORDER_BUTTON)
        self.click_to_element(OrderPageLocators.YES_BUTTON)

    def create_order(self):
        self.fill_client_info()
        self.fill_rent_info()
        self.complete_order()

    @allure.step('В появившемся окне получаем информацию по текущему заказу')
    def get_order_status(self):
        return self.get_text_from_element(OrderPageLocators.ORDER_RESULT_LABEL)

    def create_order_by_top_button(self):
        self.open_page(self.url)
        self.click_to_element(OrderPageLocators.TOP_ORDER_BUTTON)
        self.create_order()
        return self.get_order_status()

    def create_order_by_low_button(self):
        self.open_page(self.url)
        self.scroll_to_element(OrderPageLocators.LOW_ORDER_BUTTON)
        self.click_to_element_by_script(OrderPageLocators.LOW_ORDER_BUTTON)
        self.create_order()
        return self.get_order_status()
