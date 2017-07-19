import web

urls = (
    '/', 'index',
    '/wxvalid', 'wx_validation'
)

class index:
    def GET(self):
        return "Hello, welcome to PAN's webpy(vf2)"

class wx_validation:
    def GET(self):
        data=web.input()
	signature = data.signature
        timestamp = data.timestamp
        nonce = data.nonce
        token = 'wangyuweibaobei'
        echostr = data.echostr

	list = [token,timestamp,nonce]
	list.sort()
	list2 = ''.join(list)
	sha1 = hashlib.sha1()
	sha1.update(list2.encode('utf-8'))
	hashcode = sha1.hexdigest()

	if hashcode == signature:
		return echostr


app = web.application(urls, globals())
application = app.wsgifunc()
    #app.run()
