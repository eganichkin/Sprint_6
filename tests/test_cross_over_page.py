import allure
from pages.cross_over_page import CrossOverPage


class TestCrossOverPage:

    @allure.title('Проверка: если нажать на логотип Яндекса, в новом окне открывается страница Дзена')
    @allure.description('На главной странице ищем и нажимаем на логити Яндекса, проверяем, что в новом окне'
                        'через редирект откроется главная страница Дзена')
    def test_cross_over_from_yandex_logo(self, driver):
        cross_over_page = CrossOverPage(driver)
        expected_result = 'https://dzen.ru/'
        actual_result = cross_over_page.cross_over_from_yandex_logo_hyperlink(expected_result)
        assert expected_result in actual_result

    @allure.title('Проверка: если нажать на логотип Самоката, происходит переход на главную страницу сайта')
    @allure.description('На странице оформления заказа нажимаем на логитип "Самокат", '
                        'проверяем, что происходит переход на главную страницу')
    def test_cross_over_from_scooter_logo(self, driver):
        cross_over_page = CrossOverPage(driver)
        expected_result = 'https://qa-scooter.praktikum-services.ru/'
        actual_result = cross_over_page.cross_over_from_scooter_logo_hyperlink()
        assert expected_result == actual_result
