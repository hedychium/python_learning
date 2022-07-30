# encoding=utf-8

"""
__project_ = 'py-worksapce'
__file_name__ = 'historyConvert2NV&Position'
__author__ = 'li.jiang'
__time__ = '2019/8/15 16:59'
__product_name = PyCharm
# Keep calm and carry on 
"""

'将产品导入记录文件转换成净值和持仓文件'
import pandas  as pd
import xlwt

class convert:
    def convertfunc(self, filePath, sheetName):
        df = pd.read_excel(filePath, sheet_name=sheetName)#有的版本的pandas使用sheetname参数
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
            xls.save("D:/py-worksapce/Hello/Data/netValue.xls")
        elif sheetName=="持仓":
            position_data=[]
            for i in range(0,len(df)):
                data = df.loc[i, ['证券类型', '日期','证券代码',"交易所代码","证券名称",'方向','投保','数量','市值']].to_dict()
                # print(data)
                position_data.append(data)
            col_names=['日期','证券代码','交易市场代码','持仓类型','投保','持仓数量','持仓权重','价格']
            codeMap={"上交所":'XSHG',"深交所":'XSHE','场外基金':'OTC'}
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
                sheet.write(lineNumber, 3, 'LONG')#有很多种投保方向，可根据需要自行修改
                sheet.write(lineNumber, 4, None)
                sheet.write(lineNumber, 5, str(dict_item["数量"]))
                sheet.write(lineNumber, 6, None)
                sheet.write(lineNumber, 7, round(float(dict_item['市值'])/float(dict_item['数量']),2))
                lineNumber+=1
            xls.save("D:/py-worksapce/Hello/Data/position.xls")

    def test_convert(self):
        sheetnames = ["资产", "持仓"]
        c = convert()
        filePath = "D:/py-worksapce/Hello/Data/净值+持仓080808_导入历史_2018-07-29_2019-07-29.xlsx"
        c.convertfunc(filePath, sheetnames[0])
        c.convertfunc(filePath, sheetnames[1])

    def hhh(self):
        pass

if __name__=="__main__":
    sheetnames=["资产","持仓"]
    c=convert()
    filePath="./Data/甲FOF公募基金1号估值表_导入历史_2017-06-27_2018-06-27.xlsx"
    c.convertfunc(filePath,sheetnames[0])
    c.convertfunc(filePath,sheetnames[1])
