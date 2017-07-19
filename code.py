import web

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return "Hello, welcome to PAN's webpy"

if __name__ == "__main__":
    application = app.wsgifunc()
    #app = web.application(urls, globals())
    app.run()
