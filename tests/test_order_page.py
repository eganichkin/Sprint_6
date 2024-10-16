import allure
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Проверка позитивного сценария процесса создания заказа по нажатию на верхнюю кнопку "Заказать"')
    @allure.description('На главной странице сайта нажимаем на верхнюю кнопку "Заказать", в форме заполнения '
                        'информации по заказу вводим корректную информацию, сохраняем  и проверяем, что заказ оформлен')
    def test_create_order_by_top_button_check_completion_status(self, driver):
        order_page = OrderPage(driver)
        assert 'Заказ оформлен' in order_page.create_order_by_top_button()

    @allure.title('Проверка позитивного сценария процесса создания заказа по нажатию на нижнюю кнопку "Заказать"')
    @allure.description('На главной странице сайта нажимаем на нижнюю кнопку "Заказать", в форме заполнения '
                        'информации по заказу вводим корректную информацию, сохраняем  и проверяем, что заказ оформлен')
    def test_create_order_by_low_button_check_completion_status(self, driver):
        order_page = OrderPage(driver)
        assert 'Заказ оформлен' in order_page.create_order_by_low_button()
