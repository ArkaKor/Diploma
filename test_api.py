from API.api_page import APIPage
import allure


@allure.suite("Кинопоиск API")
@allure.title("Поиск фильмов по id")
@allure.description("Тест проверяет корректность поиска фильма по id")
@allure.feature("Кинопоиск API")
@allure.severity(allure.severity_level.BLOCKER)
def test_find_by_id():
    status = APIPage.find_by_id('355')
    assert status == 200


@allure.suite("Кинопоиск API")
@allure.title("Получения списка id")
@allure.description("Тест проверяет работу полуения списка id стран и жанров")
@allure.feature("Кинопоиск API")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_list_id():
    status = APIPage.get_list_id()
    assert status == 200


@allure.suite("Кинопоиск API")
@allure.title("Получение списка ТОП фильмов")
@allure.description("Тест проверяет получение списка ТОП фильмов")
@allure.feature("Кинопоиск API")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_top_list():
    status = APIPage.get_top_list()
    assert status == 200


@allure.suite("Кинопоиск API")
@allure.title("Поиск фильмов без токена")
@allure.description("Тест проверяет наличие ошибки на отсутсвие токена")
@allure.feature("Кинопоиск API")
@allure.severity(allure.severity_level.CRITICAL)
def test_find_by_filed_id():
    status = APIPage.find_by_id_no_token('777')
    assert status == 401


@allure.suite("Кинопоиск API")
@allure.title("Поиск фильмов неверным методом")
@allure.description("Тест проверяет наличие ошибки при неверном метода")
@allure.feature("Кинопоиск API")
@allure.severity(allure.severity_level.NORMAL)
def test_wrong_method():
    status = APIPage.find_by_wrong_method('355')
    assert status == 500
