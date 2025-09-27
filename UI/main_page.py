from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import allure


class MainPage():
    def __init__(self, driver):
        """
        Конструктор класса MainPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    @allure.step("Открытие главной страницы")
    def open(self):
        """
        Открывает главную страницу.
        """
        self.driver.get('https://www.kinopoisk.ru/')

    @allure.step("Поиск через таб по названию '{find}'")
    def tab_search(self, find: str):
        """
        Выбирает таб для поиска.
        Заполняет таб указанным значением.

        :param find: str - значение для поиска.
        """
        tab = self.driver.find_element(
            By.CLASS_NAME,
            'styles_input__WCRXt.kinopoisk-header-search-form-input__input'
            )
        tab.send_keys(find)
        tab.send_keys(Keys.ENTER)

    @allure.step("Переход на страницу расширенного поиска")
    def search_advanced(self):
        """
        Выполнят переход на страницу расширенного поиска.
        """
        self.driver.find_element(
            By.CLASS_NAME, 'styles_advancedSearchIcon__u9ckM'
            ).click()

    @allure.step("Переход на страницу билетов в кино")
    def tickets(self):
        """
        Выполнят переход на страницу билетов в кино.
        """
        self.driver.find_element(
            By.XPATH, "//span[text()='Билеты в кино']").click()

    @allure.step("Переход на страницу Телеканалы")
    def tvchannels(self):
        """
        Выполнят переход на страницу Телеканалы.
        """
        self.driver.find_element(
            By.XPATH, "//span[text()='Телеканалы']").click()
