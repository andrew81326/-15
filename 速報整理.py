# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 21:02:45 2021

@author: user
"""


import os
import math 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import xlsxwriter 
import xlrd 
from scipy import stats
import math
import seaborn as sns
import matplotlib.ticker as mtick
from matplotlib.ticker import FuncFormatter
from openpyxl import load_workbook


df=pd.read_excel("C://Users//user//Desktop//111.xlsx",header=0)
df.to_csv("C://Users//user//Desktop//min2020.csv")
df1=pd.read_csv("C://Users//user//Desktop//min2020.csv")
df["Test input"] = df["Test input"].astype(int)
df['Date'] = pd.to_datetime(df["Date"], format="%H:%M:%S")
df=df.drop(df[df['Test input']<=2000].index)
df= df.drop(df[df["Date"] <= "2021/02/11 12:02:00 AM"].index )
df= df.drop(df[df["Date"] >= "2021/5/20"].index)
df= df.drop(df[df["Name"] =='LLD-1PT'].index)
df= df.drop(df[df["Name"] =='LLD-2PT'].index)
df= df.drop(df[df["Name"] =='LLD-3PT'].index)
print(df)
df.to_excel("C://Users//user//Desktop//min2020.xlsx")
