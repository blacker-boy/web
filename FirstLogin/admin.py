import web
urls=(
    '/Adminlogin','Admin_Login',
    '/Homepage','Home_page'
)
app=web.application(urls,globals())
class Admin_Login:
    def GET(self):
        # print("get")
        return web.seeother('/static/login_1.html',True)
    def POST(self):
        # web.header("Access-Control-Allow-Origin", "*")
        # print("post")
        params=web.input()
        x=params['admin_id']
        y=params['password']
        x=int(x)
        y=int(y)
        if x==1001 and y==1:
            # a=Home_page()
            # a.GET()
            return True
class Home_page:
    def GET(self):
        return web.seeother('/static/Homepage.html',True)








if __name__=='__main__':
    app.run()
    print('asasas')