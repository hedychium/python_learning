# encoding=utf-8

"""
__project_ = 'py-worksapce'
__file_name__ = 'testPandas'
__author__ = 'li.jiang'
__time__ = '2019/8/20 16:56'
__product_name = PyCharm
# Keep calm and carry on 
"""

import pandas as pd
from pandas import Series
import numpy as np
import json
dir="D:/py-worksapce/Hello"
testdata=pd.read_excel(dir+"./Data/testdata.xlsx")
# print(testdata)
# cnames=['datadate','ticker','exchangecd','secoffset','bartime','closeprice','openprice','highprice','lowprice']
# testdata.columns=cnames
# print(testdata)
# print(testdata[testdata.closeprice==13.93])
# print(testdata.iloc[1:2:1,:])

# print(testdata['exchangecd'].value_counts())
# print(testdata['ticker'].value_counts())

data_df=pd.DataFrame([np.random.rand(2),np.random.rand(2),np.random.rand(2)],columns=['A','B'])
# print(pd.concat([data_df,data_df,data_df]))
# print(pd.concat([data_df,data_df,data_df],ignore_index=True))
json_data = [{'name':'wang','sal':50000,'job':'VP'},\
            {'name':'zhang','job':'Manager','report':'VP'},\
            {'name':':Li','sal':500,'report':'Manager'}]

# data_em=pd.read_json(json.dumps(json_data))
# print(data_em)
# print(data_em.reindex(columns=['job','name','report','sal']))

left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                      'key2': ['K0', 'K1', 'K0', 'K1'],
                         'A': ['A0', 'A1', 'A2', 'A3'],
                         'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                         'C': ['C0', 'C1', 'C2', 'C3'],
                         'D': ['D0', 'D1', 'D2', 'D3']})
# result = pd.merge(left, right, on=['key1', 'key2'])
# result=pd.merge(left,right,how='',on=['key1','key2'])

left1=pd.DataFrame({'A':[1,2],'B':[2,3]})
right1=pd.DataFrame({'A':[4,5,6],'B':[2,4,5]})
print(pd.merge(left1,right1,how='outer',on=['B']))

