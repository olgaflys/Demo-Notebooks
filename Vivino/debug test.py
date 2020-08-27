#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 19:52:47 2020

@author: mauritian
"""

import os
import pandas as pd
import pickle
import re
import json

os.chdir('/home/mauritian/Documents/Git/Demo Notebooks/Vivino/')

los = []
with (open("vivino_scripts.pkl", "rb")) as openfile:
    while True:
        try:
            los=pickle.load(openfile)
        except EOFError:
            break
        
los=[json.loads(re.findall(r'window.__PRELOADED_STATE__.+?= (\{\".*?\});?\n',i)[0]) for i in los]

dct={}

def exp1(ljs):
    ss=[]
    for i in ljs:
        dct,los=exp2({},i)
        ss.append(dct)
    return ss


def exp2(dct,js):
    if isinstance(js,dict):
        for j,k in js.items():
            if isinstance(k,dict):
                dct[j]={l1:exp2({},k) for l1 in k.keys()}
            else:
                dct[j]=k
                
    return dct,k

exp2(dct,los[0])