# -*- coding: utf-8 -*-
__author__ = 'Dmitriy.Dakhnovskiy'

from urllib.parse import parse_qs


class Request:
    """
    Класс запроса
    """

    @property
    def query_params(self):
        """
        Параметры запроса
        Загружается один раз при первом обращении
        :return: словарь параметров запроса
        """
        if self.__query_params is None:
            self.__query_params = parse_qs(self.__environ.get('QUERY_STRING'))
        return self.__query_params

    def __init__(self, environ):
        """
        :param environ: словарь - окружение приходящее в application из uWSGI
        """
        self.__environ = environ
        self.__query_params = None

    def __repr__(self):
        return str(self.__dict__)

    def __getattr__(self, item):
        return self.__environ[item.upper()]
