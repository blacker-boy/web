#-*- coding: UTF-8 -*-
import web
import MySQLdb
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
        x=str(x)
        y=str(y)
        print(x,y)
        db = MySQLdb.connect("localhost", port=3306, user="root", passwd="123456", db="admin_login", charset='utf8')
        cursor=db.cursor()
        # # sql="""create table adminlogin(
        # #        ID_admin char(20) not null,
        # #        password char(20))"""
        # # cursor.execute(sql)
        # # sql="""insert into adminlogin(
        # #        ID_admin,password)
        # #        values('1001','0001')"""
        # # try:
        # #     cursor.execute(sql)
        # #     db.commit()
        # # except:
        # #     db.rollback()
        sql= '''select * from adminlogin '''
        try:
            cursor.execute(sql)
            results=cursor.fetchall()
            for row in results:
                adminid = row[0]
                password = row[1]
                print(adminid, password)
                if  adminid==x  and  password==y :
                    # a=Home_page()
                    # a.GET()
                    return 1
                    break
            else:
                return False
        except:
            db.rollback()
        cursor.close()
        db.close()
        # if x=='1001' and y=='0001':
        #     # return ResponseUtil.writeToResponse(True);
        #     # a=Home_page()
        #     # a.GET()
        #     return 1
class Home_page:
    def GET(self):
        return web.seeother('/static/Homepage.html',True)

if __name__=='__main__':
    app.run()
