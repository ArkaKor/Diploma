from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure


class TVPage():
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
        Возвращает заголовок страницы "Телеканалы".

        :return: str - заголовок страницы.
        """
        return self.driver.find_element(
            By.TAG_NAME, 'h1'
            ).text
