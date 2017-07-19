import web

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return "Hello, welcome to PAN's webpy"

app = web.application(urls, globals())
application = app.wsgifunc()
    #app.run()
