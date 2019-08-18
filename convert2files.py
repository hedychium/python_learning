#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import pandas  as pd
import xlwt

class convert:
    def converfunc(self, filePath, sheetName):
        df = pd.read_excel(filePath, sheet_name=sheetName)
        if sheetName=="资产":
            netValue_data = []
            for i in range(0,len(df)):
                data = df.loc[i, ['单位净值', '日期','累计单位净值',"现金","资产规模"]].to_dict()
                netValue_data.append(data)
            col_names=['日期','资产规模','现金','单位净值',"累计单位净值"]
            xls=xlwt.Workbook()
            sheet=xls.add_sheet("Sheet1")
            #add header
            for i in range(0,len(col_names)):
                sheet.write(0,i,col_names[i])
            #add data
            for j in range(0,len(netValue_data)):
                dict_item=netValue_data[j]
                lineNumber=j+1
                sheet.write(lineNumber,0,dict_item['日期'])
                sheet.write(lineNumber,1, str(dict_item["资产规模"]))
                sheet.write(lineNumber,2,str(dict_item["现金"]))
                sheet.write(lineNumber,3, str(dict_item["单位净值"]))
                sheet.write(lineNumber,4, str(dict_item["累计单位净值"]))
            xls.save("./data/netValue.xls")
        elif sheetName=="持仓":
            position_data=[]
            for i in range(0,len(df)):
                data = df.loc[i, ['证券类型', '日期','证券代码',"交易所代码","证券名称",'方向','投保','数量','市值']].to_dict()
                position_data.append(data)
            col_names=['日期','证券代码','交易市场代码','持仓类型','投保','持仓数量','持仓权重','价格']
            codeMap={"上交所":'XSHG',"深交所":'XSHE'}
            xls = xlwt.Workbook()
            sheet = xls.add_sheet("Sheet1")
            # add header
            for i in range(0, len(col_names)):
                sheet.write(0, i, col_names[i])
            # add data
            lineNumber=1
            for j in range(0, len(position_data)):
                dict_item = position_data[j]
                if dict_item['数量']=='--':
                    continue
                sheet.write(lineNumber, 0, dict_item['日期'])
                sheet.write(lineNumber, 1, str(dict_item["证券代码"]))
                sheet.write(lineNumber, 2, codeMap[dict_item['交易所代码']])
                sheet.write(lineNumber, 3, 'LONG')
                sheet.write(lineNumber, 4, None)
                sheet.write(lineNumber, 5, str(dict_item["数量"]))
                sheet.write(lineNumber, 6, 0.01)
                sheet.write(lineNumber, 7, round(float(dict_item['市值'])/float(dict_item['数量']),2))
                lineNumber+=1
            xls.save("./data/position.xls")

# a=["资产","持仓"]
c=convert()
# filePath="./data/净值+持仓080808_导入历史_2018-07-29_2019-07-29.xlsx"
# c.converfunc(filePath,a[0])
# c.converfunc(filePath,a[1])
print(dir(c))