# -*- coding: utf-8 -*-
__author__ = 'Dmitriy.Dakhnovskiy'

from application.application import Application
from response.response import Response

app = Application()


@app.route('/')
def hello_world(request):
    """
    Пример вызова http://127.0.0.1:8080
    """
    return Response('Привет мир!', headers=[('Content-Type', 'text/plain; charset=utf-8')])


@app.route('/params')
def params(request):
    """
    Пример вызова http://127.0.0.1:8080/params?a=1;b=2;a=3
    """
    return Response('Params: {0}'.format(request.query_params))


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple(
        '127.0.0.1', 8080, app,
        use_debugger=True, use_reloader=True, processes=2,
    )
