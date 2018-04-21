#-*- coding: UTF-8 -*-
import MySQLdb
db = MySQLdb.connect("localhost", port=3306,user="root", passwd="123456", db="admin_login", charset='utf8')
cursor=db.cursor()
x='1003'
y='0002'
# sql="""create table adminlogin(
#        sex char(20) not null,
#        age int not null,
#        )"""
# cursor.execute(sql)
# sql="""insert into adminlogin(
#        ID_admin,password)
#        values('1002','0002')"""
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()
sql= '''select * from adminlogin '''
try:
    cursor.execute(sql)
    results=cursor.fetchall()
    len=len(results)
    for row in results:
      admin_id=row[0]
      password=row[1]
      if admin_id==x and password==y:
          print(admin_id,password)
          break
    else:
        print("用户名或密码不正确")
      # sex=row[2]
      # age=row[3]
      # print(admin_id,password)
except :
    db.rollback()
cursor.close()
db.close()