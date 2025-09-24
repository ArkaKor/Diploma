from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure


class SearchResultPage():
    def __init__(self, driver):
        """
        Конструктор класса SearchResultPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    @allure.step("Получение результатов поиска")
    def get_result(self) -> int:
        """
        Возвращает результаты поиска.

        :return: int - колличество найденых фильмов.
        """
        res = self.driver.find_element(
            By.CLASS_NAME, 'search_results_topText'
            ).text
        return int(res.split("результаты: ")[1])
