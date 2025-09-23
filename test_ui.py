import pytest
from selenium import webdriver
from UI.main_page import MainPage
from UI.search_advanced_page import SearchAdvancedPage
from UI.search_result_page import SearchResultPage
from UI.tickets_page import Tickets_Page
from UI.tv_page import TVPage
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.UI
@allure.suite("Кинопоиск")
@allure.title("Поиск фильмов")
@allure.description("Тест проверяет работу через таб поиска")
@allure.feature("Кинопоиск UI")
@allure.severity(allure.severity_level.CRITICAL)
def test_find_film(driver):
    """
    Тест проверяет проверяет работу через таб поиска.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    """
    main = MainPage(driver)
    main.open()
    main.tab_search("Дюймовочка")
    res = SearchResultPage(driver).get_result()
    with allure.step("Проверка полученного результата"):
        assert res >= 1


@pytest.mark.UI
@allure.suite("Кинопоиск")
@allure.title("Расширенный поиск фильмов")
@allure.description("Тест проверяет работу расширенного поиска")
@allure.feature("Кинопоиск UI")
@allure.severity(allure.severity_level.CRITICAL)
def test_advanced_find(driver):
    """
    Тест проверяет проверяет работу расширенного поиска.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    """
    main = MainPage(driver)
    main.open()
    main.search_advanced()
    SearchAdvancedPage(driver).search_film("Паруса")
    res = SearchResultPage(driver).get_result()
    with allure.step("Проверка полученного результата"):
        assert res >= 1


@pytest.mark.UI
@allure.suite("Кинопоиск")
@allure.title("Страница билетов в кино")
@allure.description("Тест доступа страницы поиска билетов в кино")
@allure.feature("Кинопоиск UI")
@allure.severity(allure.severity_level.NORMAL)
def test_open_tickets_page(driver):
    """
    Тест проверяет доступ страницы поиска билетов в кино.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    """
    main = MainPage(driver)
    main.open()
    main.tickets()
    res = Tickets_Page(driver).get_title()
    with allure.step("Проверка полученного результата"):
        assert res == 'Билеты в кино'


@pytest.mark.UI
@allure.suite("Кинопоиск")
@allure.title("Поиск билетов в кино")
@allure.description("Тест проверяет работу поиска билетов в кино")
@allure.feature("Кинопоиск UI")
@allure.severity(allure.severity_level.NORMAL)
def test_open_tickets_buy(driver):
    """
    Тест проверяет переход к покупке билета.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    """
    main = MainPage(driver)
    main.open()
    main.tickets()
    ticket = Tickets_Page(driver)
    ticket.cinema_page()
    res = ticket.get_cinema_list()
    with allure.step("Проверка полученного результата"):
        assert len(res) >= 1


@pytest.mark.UI
@allure.suite("Кинопоиск")
@allure.title("Страница 'Телеканалы'")
@allure.description("Тест доступа страницы 'Телеканалы'")
@allure.feature("Кинопоиск UI")
@allure.severity(allure.severity_level.CRITICAL)
def test_open_tvchannels(driver):
    """
    Тест проверяет переход на страницу Телеканалы.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    """
    main = MainPage(driver)
    main.open()
    main.tvchannels()
    res = TVPage(driver).get_title()
    with allure.step("Проверка полученного результата"):
        assert res == 'Смотреть каналы'
