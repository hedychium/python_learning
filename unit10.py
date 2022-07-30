#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# name=set()
# instr='abc'
# while not instr.isdigit():
#     instr=input("please input a name:")
#     if not instr.isdigit():
#         if instr in name:
#             print(" this name has  existed")
#             break
#         name.add(instr)
#
#
# print(name)

print("functions:1.add 2.delete 3.search 4.display 5.exit")

phoneDict=dict()
while True:
    instr=input("please choose a function:")
    if instr.isdigit():
        if int(instr)==1:
            name=input("please input name:")
            number=input("please input phone number:")
            if number.isdigit():
                phoneDict.setdefault(number)
                phoneDict[number]=name
                print("add success")
            else:
                print('illegel number')
            continue
        if int(instr)==2:
            number = input("please input number to delete:")
            if number in phoneDict.keys():
                del phoneDict[number]
                print("delete success")
            else:
                print('the name is not exist')
            continue
        if int(instr)==3:
            number = input("please input number to search:")
            if name in phoneDict.values():
                print("{0} {1}".format(phoneDict.get(number),number))
            else:
                print('the number is not exist')
            continue
        if int(instr)==4:
            print("all of the list:")
            for k,v in phoneDict.items():
                print("{0} {1}".format(k,v))
            continue
        if int(instr)==5:
            break
        else:
            print('illegel input')
            continue