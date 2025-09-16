import requests
import allure

my_headers = {
    'Content-Type': 'application/json',
    'X-API-KEY': 'f96df5cc-eee9-4d41-aba6-f4c9d9d1130f'
    }

url = 'https://kinopoiskapiunofficial.tech/api/v2.2/films/'


class APIPage:

    @allure.step("Поиск фильма по id")
    def find_by_id(id):
        """
        Поиск фильма по указанному id.
        Возвращает статус код ответа.

        :param id: str — идентификатор фильма.
        :return: int — статус код.
        """
        return requests.get(url+id, headers=my_headers).status_code

    @allure.step("Получение списка id")
    def get_list_id():
        """
        Получает список идентификаторов стран и жанров.
        Возвращает статус код ответа.

        :return: int — статус код.
        """
        return requests.get(url+'filters', headers=my_headers).status_code

    @allure.step("Получение списка ТОП популярных фильмов")
    def get_top_list():
        """
        Получает список ТОП популярных фильмов.
        Возвращает статус код ответа.

        :return: int — статус код.
        """
        return requests.get(
            url+'collections?Type=TOP_POPULAR_ALL', headers=my_headers
            ).status_code

    @allure.step("Поиск фильма по id без токена")
    def find_by_id_no_token(id):
        """
        Поиск фильма по указанному id без токена авторизации.
        Возвращает статус код ответа.

        :param id: str — идентификатор фильма.
        :return: int — статус код.
        """
        return requests.get(url+id).status_code

    @allure.step("Поиск фильма неверным методом")
    def find_by_wrong_method(id):
        """
        Поиск фильма неверным методом запроса.
        Возвращает статус код ответа.

        :param id: str — идентификатор фильма.
        :return: int — статус код.
        """
        return requests.post(url+id, headers=my_headers).status_code
