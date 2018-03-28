#-*- coding: UTF-8 -*-
def recursion(n,x,y,z):
    if n==1:
        print(x,'-->',z)
    else:
        recursion(n-1,x,z,y)
        print(x,'-->',z)
        recursion(n-1,y,x,z)
n=int(input('请输入汉诺塔的层数：'))
recursion(n,'x','y','z')