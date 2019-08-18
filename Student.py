#!/usr/bin/env python 
# -*- coding:utf-8 -*-

class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        if not isinstance(value,int):
            raise ValueError("not a interger!")
        if value<0:
            raise ValueError('width must big than 0')
        self._width=value

    @property
    def height(self):
        return  self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError("not a interger!")
        if value < 0:
            raise ValueError('height must big than 0')
        self._height = value

    @property
    def resolution(self):
        return self._height*self._width

s=Screen()
s.width=12
s.height=13
print(s.resolution)

class Fib(object):
    def __init__(self):
        self.a,self.b=0,1

    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>1000:
            raise StopIteration()
        return  self.a
    def __getitem__(self, n):
        a,b=1,1
        for x in range(n):
            a,b=b,a+b
        return a

# for n in Fib():
#     print(n)
#
# print(Fib()[6])


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().status.user.timeline.list)