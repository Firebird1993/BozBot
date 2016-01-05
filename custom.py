'''
Created on Jan 4, 2016

@author: lorenzo
'''

import os, random

keys = ['gio','fede','taba','chili','carme','ja','lollo','pie']

def selectAnswer(message):
    dirpath = '/home/lorenzo/Eclipse/workspace/BozBot/insulti/'
    ans = False
    msg = message.lower()
    
    for key in keys:
        if key in msg:
            path = dirpath + key + '.txt'
            lines = [line.strip() for line in open(path, 'r')]
            ans = random.choice(lines)
    
    return ans        

def selectPhoto(message):
    
    dirpath = '/home/lorenzo/Eclipse/workspace/BozBot/pictures/'
    photo = False
    msg = message.lower()
    
    for key in keys:
        if key in msg:
            dirpath = dirpath + key +'/'
            filepath = dirpath + random.choice(os.listdir(dirpath))
            photo = open(filepath,'rb')
    
    return photo