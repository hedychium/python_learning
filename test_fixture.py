# encoding=utf-8

"""
__project_ = 'py-worksapce'
__file_name__ = 'test_fixture'
__author__ = 'li.jiang'
__time__ = '2019/8/22 19:25'
__product_name = PyCharm
# Keep calm and carry on 
"""

import json
import pytest
user_json=[
  {"name":"jack","password":"Iloverose"},
  {"name":"rose","password":"Ilovejack"},
  {"name":"tom","password":"password123"}
]

class TestUserPassword(object):
    @pytest.fixture()
    def users(self):
        return user_json

    def test_user_password(self,users):
        for user in users:
            p=user["password"]
            assert len(p)>6


def foo(num):
    print("starting...")
    while num<10:
        num=num+1
        yield num
for n in foo(0):
    print(n)