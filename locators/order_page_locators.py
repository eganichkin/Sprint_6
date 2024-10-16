from selenium.webdriver.common.by import By


class OrderPageLocators:

    TOP_ORDER_BUTTON = By.XPATH, "(//button[text()='Заказать'])[1]"
    LOW_ORDER_BUTTON = By.XPATH, "(//button[text()='Заказать'])[2]"#"//button[@class='Button_Button__ra12g Button_UltraBig__UU3Lp']"

    NAME_INPUT = By.XPATH, "//div [@class = 'Order_Form__17u6u']/div[1]/input"
    SURNAME_INPUT = By.XPATH, "//div [@class = 'Order_Form__17u6u']/div[2]/input"
    ADDRESS_INPUT = By.XPATH, "//div [@class = 'Order_Form__17u6u']/div[3]/input"
    METRO_INPUT = By.XPATH, "//div [@class = 'Order_Form__17u6u']/div[4]/div/div/input"
    METRO_STATION_SELECT = By.XPATH, "(// li[@class = 'select-search__row'])[1]"
    TELEPHONE_INPUT = By.XPATH, "//div [@class = 'Order_Form__17u6u']/div[5]/input"
    NEXT_ORDER_BUTTON = By.XPATH, "//button[text()='Далее']"

    DATE_DELIVER_INPUT = By.XPATH, "//div[@class = 'react-datepicker__input-container']/input"
    DATE_DELIVER_SELECT = By.XPATH, "//div['--today' in @class][1]"
    RENTAL_PERIOD_INPUT = By.XPATH, "//span[@class = 'Dropdown-arrow']"
    RENTAL_PERIOD_SELECT = By.XPATH, "//div[@class = 'Dropdown-menu']/div[1]"
    SCOOTER_CHECKBOX = By.XPATH, "// *[ @ id = 'black']"
    COMMENT_INBOX = By.XPATH, "//input[@class = 'Input_Input__1iN_Z Input_Responsible__1jDKN']"

    COMPLETE_ORDER_BUTTON = By.XPATH, "//div[@class = 'Order_Buttons__1xGrp']/button[text()='Заказать']"
    YES_BUTTON = By.XPATH, "//button[text()='Да']"
    ORDER_RESULT_LABEL = By.XPATH, "//div[@class = 'Order_ModalHeader__3FDaJ']"
