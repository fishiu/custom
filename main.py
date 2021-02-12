import web
from handle import Handle

urls = (
    '/wx', 'Handle',
    '/wx2', 'Handle2'
)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()