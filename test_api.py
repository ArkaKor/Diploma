from API.api_page import APIPage
import pytest
import allure


url = APIPage('https://kinopoiskapiunofficial.tech/api/v2.2/films/')


@pytest.mark.API
@allure.suite("Кинопоиск")
@allure.title("Поиск фильмов по id")
@allure.description("Тест проверяет корректность поиска фильма по id")
@allure.feature("Кинопоиск API")
@allure.severity(allure.severity_level.BLOCKER)
def test_find_by_id():
    status = url.find_by_id('355')
    with allure.step("Проверка полученного результата"):
        assert status == 200


@pytest.mark.API
@allure.suite("Кинопоиск")
@allure.title("Получения списка id жанров и стран")
@allure.description("Тест проверяет работу полуения списка id стран и жанров")
@allure.feature("Кинопоиск API")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_list_id():
    status = url.get_list_id()
    with allure.step("Проверка полученного результата"):
        assert status == 200


@pytest.mark.API
@allure.suite("Кинопоиск")
@allure.title("Получение списка ТОП фильмов")
@allure.description("Тест проверяет получение списка ТОП фильмов")
@allure.feature("Кинопоиск API")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_top_list():
    status = url.get_top_list()
    with allure.step("Проверка полученного результата"):
        assert status == 200


@pytest.mark.API
@allure.suite("Кинопоиск")
@allure.title("Поиск фильмов без токена")
@allure.description("Тест проверяет наличие ошибки на отсутсвие токена")
@allure.feature("Кинопоиск API")
@allure.severity(allure.severity_level.CRITICAL)
def test_find_no_token():
    status = url.find_by_id_no_token('777')
    with allure.step("Проверка полученного результата"):
        assert status == 401


@pytest.mark.API
@allure.suite("Кинопоиск")
@allure.title("Поиск фильмов неверным методом")
@allure.description("Тест проверяет наличие ошибки при неверном метода")
@allure.feature("Кинопоиск API")
@allure.severity(allure.severity_level.NORMAL)
def test_wrong_method():
    status = url.find_by_wrong_method('355')
    with allure.step("Проверка полученного результата"):
        assert status == 500
