from selenium.webdriver.common.by import By


class MainPageLocators:

    QUESTION_LOCATOR = By.XPATH, "//*[@id='accordion__heading-{}']"
    ANSWER_LOCATOR = By.XPATH, "//*[@id='accordion__panel-{}']"

    COOKIES_BUTTON = By.XPATH, "//button[text() = 'да все привыкли']"

