#!/usr/bin/env python
# coding: utf-8

# ## STAT 507 Problem Set 4
# ## Name: Yang Li (46933158)
# ## Email: yangyli@umich.edu
# > ## Question 0 - Topics in Pandas [25 points]
# 

# In[1]:


import pandas as pd
import numpy as np
import datetime
from scipy.stats import norm
import matplotlib.pyplot as plt
import math
from scipy import stats


# ## Time series
# - Pandas contains extensive capabilities and features for working with time series data for all domains.
# - Parsing time series information from various sources and formats.

# In[2]:


dti = pd.to_datetime(["1/1/2021", 
                      np.datetime64("2021-01-01"), 
                      datetime.datetime(2021, 1, 1)])
dti


# ## Time series
# - Generate sequences of fixed-frequency dates and time spans.
# - Manipulating and converting date times with timezone information.
# 

# In[3]:


dti = pd.date_range("2021-01-01", periods=2, freq="H")
print(dti)
dti1 = dti.tz_localize("UTC")
print(dti1)
dti1.tz_convert("US/Pacific")


# ## Time series
# 
# - Resampling or converting a time series to a particular frequency.

# In[4]:


idx = pd.date_range("2021-01-01", periods=4, freq="H")
ts = pd.Series(range(len(idx)), index=idx)
ts


# ## Time series
# 
# - Performing date and time arithmetic with absolute or relative time increments.

# In[5]:


friday = pd.Timestamp("2021-10-22")
print(friday.day_name())
# Add 1 day
saturday = friday + pd.Timedelta("1 day")
print(saturday.day_name())
