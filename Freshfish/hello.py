import  web
from Freshfish import blog

urls=(
    '/blog', blog.app_blog,
    '/(.*)','index'
)
class index:
    def GET(self,path):
        return 'hello'+path
app=web.application(urls,globals())
if __name__=='__main__':
    app.run()
# m=globals()
# print(globals())