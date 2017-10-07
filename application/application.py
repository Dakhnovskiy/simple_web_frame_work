# -*- coding: utf-8 -*-
__author__ = 'Dmitriy.Dakhnovskiy'

from request.request import Request
from response.response import Response


class Application:

    def __init__(self):
        self.__routing_dict = {}

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
        return self.__routing_dict[path_info]

    def add_response_function(self, path_info, response_function):
        """
        Добавить функцию-ответ соответствующую path_info
        :param path_info: Остаток пути в URL соответствующий цели запроса внутри приложения
        :param response_function: функция-ответ
        """
        self.__routing_dict[path_info] = response_function
