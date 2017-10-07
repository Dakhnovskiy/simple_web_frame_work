# -*- coding: utf-8 -*-
__author__ = 'Dmitriy.Dakhnovskiy'


class Response:
    """
    Класс ответа
    """
    __default_status = '200 OK'
    __empty_response = b''

    def __init__(self, response=None, status=None, headers=None):
        """
        :param response: тело ответа
        :param status: статус ответа
        :param headers: заголовки ответа
        """
        self.__response = self.__empty_response if response is None else response
        self.__status = self.__default_status if status is None else status
        self.__headers = [] if headers is None else headers

    def __call__(self, start_response):
        """
        :param start_response: callable - объект переданный uWSGI
        :return: тело ответа
        """
        start_response(self.__status, self.__headers)
        return [self.__response]
