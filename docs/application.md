## Класс Application
Класс web-приложение

##Методы:
* add_response_function(self, path_info, response_function)

    Добавить функцию-ответ соответствующую path_info
    * path_info: Остаток пути в URL соответствующий цели запроса внутри приложения
    * response_function: функция-ответ
        

* route(self, path_info)

    Метод возвращающий декоратор для регистрации функций-ответов