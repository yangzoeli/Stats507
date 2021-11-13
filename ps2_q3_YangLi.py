#!/usr/bin/env python
# coding: utf-8
# %%

# ## STAT 507 Problem Set 2
# ## Name: Yang Li (46933158)

# modules: -------------------------------------
import numpy as np
import pandas as pd
import random
import timeit
import json
import matplotlib.pyplot as plt
#from itertools import combinations_with_replacement, product
# ----------------------------------------------

# ## Question 3
# a) Use Python and Pandas to read and append the demographic datasets keeping certain columns.

# %%

# load the data ----------------------------------
demo1112 = pd.read_sas("DEMO_G.XPT")
demo1314 = pd.read_sas("DEMO_H.XPT")
demo1516 = pd.read_sas("DEMO_I.XPT")
demo1718 = pd.read_sas("DEMO_J.XPT")

# add cohort id ----------------------------------
demo1112["COHORT"] = '2011_12'
demo1314["COHORT"] = '2013_14'
demo1516["COHORT"] = '2015_16'
demo1718["COHORT"] = '2017_18'
#print(demo1718.head().shape)

#combine these four files ------------------------
demo11_18 = pd.concat([demo1112, demo1314, demo1516, demo1718], axis=0)

# To get certain columns ------------------------
column_u1 = ["COHORT","SEQN", "RIAGENDR","RIDAGEYR", "RIDRETH3", "DMDEDUC2",
            "DMDMARTL", "RIDSTATR", "SDMVPSU", "SDMVSTRA", "WTMEC2YR", "WTINT2YR"]

#column_d1 =[x.lower() for x in column_u1 if isinstance(x,str)]
demo = demo11_18[column_u1]

#rename the column names using all lower case ----
demo.columns = demo.columns.map(lambda x:x.lower())

#convert to a category type -----------------------
demo = demo.astype("category")

#save the data to a  format -----------------------
demo.to_pickle('demo.pkl')


# b) Repeat part a for the oral health and dentition data (OHXDEN_*.XPT) retaining the following variables: SEQN, OHDDESTS, tooth counts (OHXxxTC), and coronal cavities (OHXxxCTC).

# %%


'''
--- Attempt to read from the websites (failed)---
import pandas as pd
ohxcen12 = pd.read_html('https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/OHXDEN_G.htm')
ohxcen34 = pd.read_html('https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/OHXDEN_H.htm')
ohxcen56 = pd.read_html('https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/OHXDEN_I.htm')
ohxcen78 = pd.read_html('https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/OHXDEN_J.htm')
ohxcen1112 = pd.DataFrame.from_records(ohxcen12)
'''

# load the data ----------------------------------
ohxden1112 = pd.read_sas("OHXDEN_G.XPT")
ohxden1314 = pd.read_sas("OHXDEN_H.XPT")
ohxden1516 = pd.read_sas("OHXDEN_I.XPT")
ohxden1718 = pd.read_sas("OHXDEN_J.XPT")

# add cohort id ----------------------------------
ohxden1112["COHORT"] = '2011_12'
ohxden1314["COHORT"] = '2013_14'
ohxden1516["COHORT"] = '2015_16'
ohxden1718["COHORT"] = '2017_18'

#combine these four files ------------------------
ohxden11_18 = pd.concat([ohxden1112, ohxden1314, ohxden1516, ohxden1718], axis=0)

# To get the names of certain columns --------------------
# ohx01-32Tc ohx02-31ctc(without16-17)
#ohcolist = ohxden11_18.columns.tolist()
#str_match = list(filter(lambda x: 'SEQN' or 'OHDDESTS' and \
#                        (x.startswith('OHX') and (endswith('TC') or endswith('CTC'))), ohcolist))
# This commond gives more than the expected eg.OHXxxRTC ...

c1s = []
c2s = []
for i in range(1,33,1):
    if i<10:
        c1 = 'OHX0'+ str(i) +'TC'
        c2 = 'OHX0'+ str(i) +'CTC'
    else:
        c1 = 'OHX'+ str(i) +'TC' 
        c2 = 'OHX'+ str(i) +'CTC'        
    c1s.append(c1)
    c2s.append(c2)
#c2s[1:-1]
c2s.remove('OHX16CTC')
c2s.remove('OHX17CTC') #does not contain 16-17 columns

column_u2 = ['COHORT','SEQN', 'OHDDESTS'] + c1s + c2s[1:-1] 
#column_d2 =[x.lower() for x in column_u2 if isinstance(x,str)]

# To keep certain columns ------------------------
ohxden = ohxden11_18[column_u2]

#rename the column names using all lower case ----
ohxden.columns = ohxden.columns.map(lambda x:x.lower())

#convert to a category type -----------------------
ohxden = ohxden.astype("category")

#save the data to a  format -----------------------
ohxden.to_pickle('ohxden.pkl')


# c) report the number of cases there are in the two datasets above

# %%


print('q3a shape',demo.shape)
print('q3b shape',ohxden.shape)


# %%




