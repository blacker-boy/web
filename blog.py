import  web
urls=(
    '','reblog',
    '/(.*)','blog'
)
class reblog:
    def GET(self):
        print(5)
        raise web.seeother('/')
class blog:
    def GET(self,path):
        return 'blog'+path
app_blog=web.application(urls,globals())
