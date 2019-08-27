# encoding=utf-8

"""
__project_ = 'py-worksapce'
__file_name__ = 'check'
__author__ = 'li.jiang'
__time__ = '2019/8/23 22:11'
__product_name = PyCharm
# Keep calm and carry on 
"""

with open("D:\\py-worksapce\\auto_algorithm\\Storm\\puma_research_pdf_parser\\yanbaoke-08-23-3.log",encoding='utf-8') as f:
    i=0
    for line in f:
        if i<5:
            arr = line.split('\t')
            print(arr)
        i+=1