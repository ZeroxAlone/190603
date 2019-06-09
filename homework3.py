# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 19:08:36 2019

@author: translucky
"""

'''
不会
'''
import matplotlib.pyplot as plt

image=[]
width=640
height=640
def zero(image,width,height):
    #image.clear()
    for i in range(height):
        image.append([0]*width)
        zero(image,width-1,height-1)
zero(image,width,height)
plt.imshow(image,cmap="gray",vmin=0,vmax=255)
plt.show()

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    a=[]
    p=0
    for i in aDict:
        a.append(aDict[i])
    for j in a:
        for l in j:
            p+=1
    return p
print(how_many(animals))

def biggest(aDict):
    n=max(aDict,key=aDict.get)
    return n
print(biggest(animals))