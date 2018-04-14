#-*- coding: UTF-8 -*-
# dict1={"李宁":"一切皆有可能","耐克":"just do it","阿迪达斯":"impossible is nothing","鱼C工作室":"让编程改变世界"}
# # print('鱼C工作室的口号',dict1["鱼C工作室"])
# print("李宁的广告词是：",dict1["李宁"])
adict = {}
bdict = {'name':'miss','sex':'gril'}
print(cmp(adict, bdict))
print(bdict.pop('name'))
print(bdict.get('sex'))
adict=bdict
print(bdict.clear())
print(adict.get('name'))
