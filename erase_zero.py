#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import pymysql

money_all=56.75+2+938.7+83.2
money_all_str=str(money_all)
print(money_all_str)

money_real=int(money_all)
print(str(money_real))

print(7/3)
print(7//5)


print(35<54)

def sort(x):
    return x['price']


mydb=pymysql.connect(
    host="localhost",
    user='root',
    password="123456",
)
cursor=mydb.cursor()
sqltext='show databases'
cursor.execute(sqltext)
for row in cursor:
    print(row)
