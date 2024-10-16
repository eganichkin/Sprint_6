from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure


class BasePage:
    timeout = 10
    url = 'https://qa-scooter.praktikum-services.ru/'

    @staticmethod
    def format_locators(locator_before_format, num):
        method, locator = locator_before_format
        locator = locator.format(num)
        return method, locator

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем веб-страницу {url}')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Получаем текущий адрес веб-страницы')
    def current_url(self):
        return self.driver.current_url

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, self.timeout).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Кликаем по элементу')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, self.timeout).until(expected_conditions.visibility_of_element_located(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Кликаем по элементу')
    def click_to_element_by_script(self, locator):
        WebDriverWait(self.driver, self.timeout).until(expected_conditions.visibility_of_element_located(locator))
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Получает текст элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Скроллим до элемента')
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Записываем текст {text} в элемент')
    def send_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    @allure.step('Ожидаем выполнения редиректа на адрес {expected_url}')
    def wait_for_redirect(self, expected_url):
        WebDriverWait(self.driver, self.timeout).until(lambda driver: len(driver.window_handles) != 1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, self.timeout).until(lambda driver: expected_url in self.driver.current_url)
