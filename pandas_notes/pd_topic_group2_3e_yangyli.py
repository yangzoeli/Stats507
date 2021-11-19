########################### pd_topic_group2_4j_aayushi #############################
# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     notebook_metadata_filter: markdown
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# ## Topics in Pandas
# **Stats 507, Fall 2021**
#

# ## Contents
# Add a bullet for each topic and link to the level 2 title header using
# the exact title with spaces replaced by a dash.
#
# + [Topic Title](#Topic-Title)
# + [Topic 2 Title](#Topic-2-Title)

# ## Topic Title
# Include a title slide with a short title for your content.
# Write your name in *bold* on your title slide.


# Aayushi Sinha
#
# aayushi@umich.edu
#
#
# ##  Timedeltas in Pandas

# ### Class pd.Timedelta
#
# * It represents a duration of time or date. Easy to use for date or time manipulations.
# * It is a similar to the python class of datetime.timedelta.
# * It is expressed in difference units, e.g. days, hours, minutes, seconds.

# In[1]:


import pandas as pd
from datetime import datetime, timedelta

#Calculating the number of days between two dates.
present_date = datetime.now()
print ("Present Date", str(present_date))
future_date = present_date + timedelta(days = 6)
print("Future Date", str(future_date) )

print("Days left", str(present_date - future_date))


# ### Parsing
# * Prasing through a string or an integer with units in the argument can create a timedelta object.
# * pd.to_timedelta can convert a scalar, array, list, or series from a recognized timedelta
#   format/ value into a Timedelta type.

# In[3]:


#Parsing and to_timedelta
print (pd.Timedelta('2 days 2 hours 15 minutes 30 seconds'))
#Converting to timedelta object
pd.to_timedelta("1 days 06:05:01.00003")


# ### Operations
#
# * You can construct timedelta64[ns] Series/Dataframes through subtraction operations and operate on the series/dataframes.
# * NaT values are supported in timedelta series.
# * min, max and the corresponding idxmin, idxmax operations are supported. Even negate can be used.

# In[5]:


# Operation Examples
s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
df = pd.DataFrame(dict(A = s, B = td))
df['C']=df['A']+df['B']
df['D']=df['C']-df['B']
print(df)


############################ pd_topic_group2_4i_lydiajr ##############################

# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     notebook_metadata_filter: markdown
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# ## Topics in Pandas
# **Stats 507, Fall 2021**
#

# ## Contents
# Add a bullet for each topic and link to the level 2 title header using
# the exact title with spaces replaced by a dash.
#
# + [Topic Title](#Topic-Title)
# + [Topic 2 Title](#Topic-2-Title)

# ## Topic Title
# Include a title slide with a short title for your content.
# Write your name in *bold* on your title slide.

#!/usr/bin/env python
# coding: utf-8

# + [Timedeltas: Representing changes in time](#Topic-Title)
# *Lydia Rogers*, lydiajr@umich.edu
#
# Reference for timedeltas can be found [here](https://pandas.pydata.org/pandas-docs/stable/user_guide/timedeltas.html)

# ## Intro to Timedeltas
# * In addition to the datetime functionality that works well with pandas, there are occasions where we will want to analyze changes in time rather than dates.
# * We can represent these changes in time as timedeltas using the `datetime` module in addition to pandas.

# In[1]:


# Load required modules
import pandas as pd
import datetime

# Initializing timedeltas
# Can initialize using pd.Timedelta...
t1 = pd.Timedelta("2 days")
t2 = pd.Timedelta(2, unit = "d")
print(t1 == t2)

# null = NaT
t3 = pd.Timedelta("nan")
t4 = pd.Timedelta("nat")
print(t3, t4)

# negative times also supported
t5 = pd.Timedelta("-1us")
t6 = pd.Timedelta("-3hr")
print(t5, t6)


# ... or from a time string using to_timedelta
t7 = pd.to_timedelta("1 days 06:05:01.00003")
t8 = pd.to_timedelta("247ms")
print(t7, t8)


# ## Operations using timedeltas
# * Timedeltas can be used in arithmetic operations such as addition and subtraction with other timedeltas or datetimes, as well as in scalar multiplication.
# * Other operations supported include minimum and maximum calculations, and absolute values.
# * We can convert timedeltas to different scales (hours, minutes, seconds) by dividing one timedelta object by another.

# In[2]:


# Create example dataframe
sundays = pd.Series(pd.date_range("2021-10-24", periods=6, freq="W"))
td = pd.Series([pd.Timedelta(days=i*7) for i in range(6)])
df = pd.DataFrame({"dates": sundays, "days": td})

# Timedelta arithmetic
df["new_date"] = df["dates"] + 2 * df["days"]
df["new_timedelta"] = df["dates"] - df["new_date"]
df["scaled_timedelta"] = df["new_timedelta"] * 0.4
df["seconds_timedelta"] = df["scaled_timedelta"] / pd.Timedelta(1, "s")
print(df)

# Additional operations
print("min:", df["new_date"].min())
print("max:", df["new_date"].max())
print(abs(df["new_timedelta"]))


# ## Summarizing Timedeltas
# * Timedeltas and datetimes are also supported by most reduction operations such as mean, median, quantile, and sum.
# * These reduction operations, implemented in pandas, offer easy ways to summarize changes in time.

# In[3]:


print("mean timedelta:", df["seconds_timedelta"].mean())
print("mean date:", df["new_date"].mean())

print("median timedelta:", df["seconds_timedelta"].median())
print("median date:", df["new_date"].median())

print("timedelta 75th quantile:", df["seconds_timedelta"].quantile(0.75))
print("date 75th quantile:", df["new_date"].quantile(0.75))

print("timedelta sum:", df["seconds_timedelta"].sum())


############################ pd_topic_yangyli ##############################

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
