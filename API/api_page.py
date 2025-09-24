import requests
import allure

my_headers = {
    'Content-Type': 'application/json',
    'X-API-KEY': ''
    }


class APIPage:
    def __init__(self, url):
        """
        Конструктор класса APIPage.

        :param url: str - адрес для тестирования API.
        """
        self.url = url

    @allure.step("Поиск фильма по id '{id}'")
    def find_by_id(self, id):
        """
        Поиск фильма по указанному id.
        Возвращает статус код ответа.

        :param id: str — идентификатор фильма.
        :return: int — статус код.
        """
        return requests.get(self.url+id, headers=my_headers).status_code

    @allure.step("Получение списка id")
    def get_list_id(self):
        """
        Получает список идентификаторов стран и жанров.
        Возвращает статус код ответа.

        :return: int — статус код.
        """
        return requests.get(self.url+'filters', headers=my_headers).status_code

    @allure.step("Получение списка ТОП популярных фильмов")
    def get_top_list(self):
        """
        Получает список ТОП популярных фильмов.
        Возвращает статус код ответа.

        :return: int — статус код.
        """
        return requests.get(
            self.url+'collections?Type=TOP_POPULAR_ALL', headers=my_headers
            ).status_code

    @allure.step("Поиск фильма по id '{id}' без токена")
    def find_by_id_no_token(self, id):
        """
        Поиск фильма по указанному id без токена авторизации.
        Возвращает статус код ответа.

        :param id: str — идентификатор фильма.
        :return: int — статус код.
        """
        return requests.get(self.url+id).status_code

    @allure.step("Поиск фильма неверным методом")
    def find_by_wrong_method(self, id):
        """
        Поиск фильма неверным методом запроса.
        Возвращает статус код ответа.

        :param id: str — идентификатор фильма.
        :return: int — статус код.
        """
        return requests.post(self.url+id, headers=my_headers).status_code
