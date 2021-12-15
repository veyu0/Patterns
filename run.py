from wsgiref.simple_server import make_server
from faith_framework.main import Framework
from urls import fronts
from views import routes

application = Framework(routes, fronts)
PORT = 8000

with make_server('', PORT, application) as httpd:
    print(f'Запуск сервера на порту {PORT}')
    httpd.serve_forever()
