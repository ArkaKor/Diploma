from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import allure


class TicketsPage():
    def __init__(self, driver):
        """
        Конструктор класса TicketsPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    @allure.step("Получение заголовка страницы")
    def get_title(self) -> str:
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
        tab = self.driver.find_element(
                By.CLASS_NAME, 'style_buttonAccent__Ha79h'
                )
        tab.send_keys(Keys.DOWN)
        button = self.driver.find_element(
                By.CLASS_NAME, 'styles_afishaButtonIcon__Nt5nr'
                )
        button.click()

    @allure.step("Полуение списка кинотеатров")
    def get_cinema_list(self) -> list:
        """
        Возвращает список кинотатров, доступных для выбора.

        :return: list - список кинотеатров.
        """
        return self.driver.find_elements(
            By.CLASS_NAME, 'schedule-item'
            )
