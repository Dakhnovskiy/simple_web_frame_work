# -*- coding: utf-8 -*-
__author__ = 'Dmitriy.Dakhnovskiy'

from request.request import Request
from response.response import Response


class Application:
    """
    Класс web-приложение
    """

    def __init__(self):
        self.__routing_map = {}

    def __call__(self, environ, start_response):
        """
        :param environ: словарь - окружение приходящее в application из uWSGI
        :param start_response: callable - объект переданный uWSGI
        :return: тело ответа
        """
        requset = Request(environ)
        response = self.__get_response_function(requset.path_info)(requset)
        assert isinstance(response, Response), 'response must be Response'
        return response(start_response)

    def __get_response_function(self, path_info):
        """
        Получить функцию-ответ по path_info
        :param path_info: Остаток пути в URL соответствующий цели запроса внутри приложения
        :return: функция
        """
        return self.__routing_map[path_info]

    def add_response_function(self, path_info, response_function):
        """
        Добавить функцию-ответ соответствующую path_info
        :param path_info: Остаток пути в URL соответствующий цели запроса внутри приложения
        :param response_function: функция-ответ
        """

        # TODO: exception for 404
        self.__routing_map[path_info] = response_function

    def route(self, path_info):
        """
        Метод возвращающий декоратор для регистрации функций-ответов
        """
        def decorator(response_function):
            self.add_response_function(path_info, response_function)
            return response_function
        return decorator
