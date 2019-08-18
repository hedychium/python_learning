#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# class Swan:
#     '''天鹅类'''
#     _neck_swan='long neck' #protected property
#
#     def __init__(self):
#         self.__halo='jdjj'
#         self.see='hhh'
#         print("__init_():",Swan._neck_swan)
#
# swan=Swan()
# # print("__Halo__",swan.__halo__)
# print("直接访问：",swan._neck_swan)
# print("直接访问：",swan._Swan__halo)
# print("直接访问：",Swan.see)


import sys

class Record:
    def __init__(self,date,amount,balance,tradefun,currency='人民币'):
        self.date=date
        self.amount=amount
        self.balance=balance
        self.currency=currency
        # self.abstract=abstract
        if tradefun=="add":
            self.abstract = "转入"
        elif tradefun=='pay':
            self.abstract="消费"
        elif tradefun=="outFromNet":
            self.abstract="网转"


class Trade:
    def __init__(self):
        self.balance=0
        self.tradeRecords=list()

    def add(self,date,amount):
        self.balance+=amount
        record=Record(date,amount,self.balance,sys._getframe().f_code.co_name)

        self.tradeRecords.append(record)

    def pay(self,date,amount):
        self.balance -= amount
        record = Record(date, -1*amount, self.balance, sys._getframe().f_code.co_name)
        self.tradeRecords.append(record)

    def outFromNet(self, date, amount):
        self.balance -= amount
        record = Record(date, -1*amount, self.balance, sys._getframe().f_code.co_name)
        self.tradeRecords.append(record)
        # print(sys._getframe().f_code.co_name)

    def showRecords(self):
        print("date","abstract","amount","currency","balance",sep='   ')
        for record in self.tradeRecords:
            print(record.date,record.abstract,record.amount,record.currency,record.balance,sep='   ')

trade=Trade()
trade.add("2019-01-01",1314)
trade.pay("2019-03-01",123)
trade.outFromNet("2019-05-01",87)
trade.showRecords()

def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        print(a, '-->', c)
        move(n-1, b, a, c)

move(2,'a',"b","c")
