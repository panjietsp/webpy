import web

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return "Hello, welcome to PAN's webpy"

if __name__ == "__main__":
    app = web.application(urls, globals())
    application = app.wsgifunc()
    #app.run()
