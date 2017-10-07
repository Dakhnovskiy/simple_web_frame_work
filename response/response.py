# -*- coding: utf-8 -*-
__author__ = 'Dmitriy.Dakhnovskiy'


class Response:

    def __init__(self, response=None, status=None, headers=None):
        """
        :param response: тело ответа
        :param status: статус ответа
        :param headers: заголовки ответа
        """
        self.__response = response
        self.__status = status
        self.__headers = headers

    def __call__(self, start_response):
        """
        :param start_response: callable - объект переданный uWSGI
        :return: тело ответа
        """
        start_response(self.__status, self.__headers)
        return self.__response
