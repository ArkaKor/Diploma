from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure


class SearchAdvancedPage():
    def __init__(self, driver):
        """
        Конструктор класса SearchAdvancedPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    @allure.step("Поиск по названию '{find}'")
    def search_film(self, find: str):
        """
        Заполняет форму поиска фильмов.

        :param find: str - значение для поиска.
        """
        self.driver.find_element(By.ID, 'find_film').send_keys(find)
        self.driver.find_element(By.CLASS_NAME, 'el_18.submit.nice_button'
                                 ).click()
