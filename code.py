import web
import hashlib
import reply
import receive

urls = (
    '/hello', 'hello_working_test',
    '/wxvalid', 'wx_validation',
    '/handle', 'Handle'
)

class hello_working_test:
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

class Handle(object):
    def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is ", webData   #print log on back
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = "test"
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            else:
                print "not trating now"
                return "success"
        except Exception, Argment:
            return Argment


app = web.application(urls, globals())
application = app.wsgifunc()
    #app.run()
