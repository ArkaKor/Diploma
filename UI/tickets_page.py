from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure


class Tickets_Page():
    def __init__(self, driver):
        """
        Конструктор класса Form_Page.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Получение заголовка страницы")
    def get_title(self):
        """
        Возвращает заговок страницы "Билеты в кино".

        :return: str - заголовок страницы.
        """
        title = self.driver.find_element(
            By.CLASS_NAME, 'styles_title__9HPZ9').get_attribute("textContent")
        return str(title)

    @allure.step("Переход на страницу выбора кинотеатра")
    def cinema_page(self):
        """
        Переходит на страницу выбора кинотеатра.
        """
        self.driver.find_element(
            By.CLASS_NAME,
            'style_button__Awsrq.style_buttonSize24__GACpt'
            ).click()

    @allure.step("Полуение списка кинотеатров")
    def get_cinema_list(self):
        """
        Возвращает список кинотатров, доступных для выбора.

        :return: list - список кинотеатров.
        """
        return self.driver.find_elements(
            By.CLASS_NAME, 'schedule-item'
            )
