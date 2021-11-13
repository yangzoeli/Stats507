#!/usr/bin/env python
# coding: utf-8

# ## STAT 507 Problem Set 1
# ## Name: Yang Li (46933158)

# # Answer to Question 0 - Markdown warmup
# This is *question 0* for [<font color = red>problem set 1</font>](https://jbhender.github.io/Stats507/F21/ps/ps1.html) of [<font color = red>Stats 507</font>](https://jbhender.github.io/Stats507/F21/syllabus.html).
# > ## Question 0 - Markdown warmup
# 
# The next question is about the **Fibonnaci sequence**, F<sub>n</sub>=F<sub>n-2</sub>+F<sub>n-1</sub>.
# In part **a** we will define a Python function `fib_rec()`.
# 
# Below is a …
# 
# ## Level 3 Header
# Next, we can make a bulleted list:
# 
# - Item 1
#    - detail 1
#    - detail 2
# - Item 2
# 
# Finally, we can make an enumerated list:
# 
#     a.Item 1  
#     b.Item 2  
#     c.Item 3  

# # Answer to Question 1 - Fibonnaci Sequence

# In[1]:


##-----  a.recursive function  -----##

#Write a recursive function fib_rec() 
#that takes input n

def fib_rec(n): 
    fib0 = 0
    fib1 = 1
    if n == 0: 
        return fib0
    if n == 1:
        return fib1
    if n > 1:
        return fib_rec(n-2) + fib_rec(n-1)
    
if __name__ == '__main__':
    print('F7 =', fib_rec(7))
    print('F11 =', fib_rec(11))
    print('F13 =', fib_rec(13))


# In[2]:


##-----  b.for loop -----##

# Write a function fib_for() 
# with the same signature that computes Fn 
# by summation using a for loop.

def fib_for(n): 
    if n <= 2: 
        return n
    else:
        fib1 = 1
        fib2 = 2
        for _ in range(3,n):
            fib1,fib2 = fib2, fib1+fib2
        return fib2
    
if __name__ == '__main__':
    print('F7 =', fib_for(7))
    print('F11 =', fib_for(11))
    print('F13 =', fib_for(13))


# In[3]:


##-----  c.while loop -----##

#Write a function fib_whl() 
#with the same signature that computes Fn 
#by summation using a while loop.
def fib_whl(n): 
    while n <= 2: 
        return n
    else:
        fib1 = 1
        fib2 = 2
        for _ in range(3,n):
            fib1,fib2 = fib2, fib1+fib2
        return fib2
    
if __name__ == '__main__':
    print('F7 =', fib_whl(7))
    print('F11 =', fib_whl(11))
    print('F13 =', fib_whl(13))


# In[4]:


##-----  d.rounding method -----##

#Write a function fib_rnd() 
#with the same signature that computes Fn 
#using the rounding method described on the Wikipedia page.

from math import sqrt
def fib_rnd(n):
    fai = (1+sqrt(5))/2
    return (fai**n)/(sqrt(5))
   
if __name__ == '__main__':
    print('F7 =', fib_rnd(7))
    print('F11 =', fib_rnd(11))
    print('F13 =', fib_rnd(13))


# In[5]:


##-----  e.truncation method  -----##

#Write a function fib_flr() 
#with the same signature that computes Fn 
#using the truncation method described on the Wikipedia page.


def fib_flr(n): 
    fai = (1+sqrt(5))/2
    return (fai**n)/(sqrt(5))+1/2
    
if __name__ == '__main__':
    print('F7 =', fib_flr(7))
    print('F11 =', fib_flr(11))
    print('F13 =', fib_flr(13))


# f. For a sequence of increasingly large values of n compare the median computation time of each of the functions above. Present your results in a nicely formatted table. (Point estimates are sufficient).

# In[6]:

# modules: --------------------------------------------------------------------
import numpy as np
import numpy as np
import time
import prettytable as pt

ns = np.array([10, 15, 20, 30, 40])

fib_rec_ts = []; fib_recs = []
fib_for_ts = []; fib_fors = []
fib_whl_ts = []; fib_whls = []
fib_rnd_ts = []; fib_rnds = []
fib_flr_ts = []; fib_flrs = []

for each_n in ns:
    
    # recursive function   
    start = time.time()    
    fib_rec1 = fib_rec(each_n)  
    end = time.time()
    fib_rec_t = end - start 
    fib_recs.append(fib_rec1)
    fib_rec_ts.append(fib_rec_t)

    # for loop 
    start = time.time() 
    fib_for1 = fib_for(each_n)
    end = time.time()
    fib_for_t = end - start
    fib_fors.append(fib_for1)
    fib_for_ts.append(fib_for_t)
    
    #while loop 
    start = time.time() 
    fib_whl1 = fib_whl(each_n)
    end = time.time()
    fib_whl_t = end - start
    fib_whls.append(fib_whl1)
    fib_whl_ts.append(fib_whl_t)
    
    #rounding method 
    start = time.time() 
    fib_rnd1 = fib_rnd(each_n)
    end = time.time()
    fib_rnd_t = end - start
    fib_rnds.append(fib_rnd1)
    fib_rnd_ts.append(fib_rnd_t)
    
    #truncation method 
    start = time.time() 
    fib_flr1 = fib_flr(each_n)
    end = time.time()
    fib_flr_t = end - start
    fib_flrs.append(fib_flr1)
    fib_flr_ts.append(fib_flr_t)
    
'''    
table = pt.PrettyTable()
table.add_column = ["method", "recursive function","for loop","while loop",\
                    "rounding method ","truncation method "]

for i in np.arange(0, len(ns)-1):
    table.add_column(ns[i],fib_recs[i],fib_fors[i],fib_whls[i],fib_rnds[i],fib_flrs[i])
    
table.add_column = ["median computation time", np.median(fib_recs),np.median(fib_fors),\
                    np.median(fib_whls),np.median(fib_rnds),np.median(fib_flrs)]

print(table)
'''
table = pt.PrettyTable()
table.field_names = ["method", "recursive function","for loop","while loop",                    "rounding method ","truncation method "]
table.add_row([ns[0],fib_recs[0],fib_fors[0],fib_whls[0],fib_rnds[0],fib_flrs[0]])
table.add_row([ns[1],fib_recs[1],fib_fors[1],fib_whls[1],fib_rnds[1],fib_flrs[1]])
table.add_row([ns[2],fib_recs[2],fib_fors[2],fib_whls[2],fib_rnds[2],fib_flrs[2]])
table.add_row([ns[3],fib_recs[3],fib_fors[3],fib_whls[3],fib_rnds[3],fib_flrs[3]])
table.add_row([ns[4],fib_recs[4],fib_fors[4],fib_whls[4],fib_rnds[4],fib_flrs[4]])

table.add_row(["median computation time", np.median(fib_rec_ts),np.median(fib_for_ts),                   np.median(fib_whl_ts),np.median(fib_rnd_ts),np.median(fib_flr_ts)])

print(table)


# # Answer to Question 2 - Pascal’s Triangle

# In[7]:


##-----  a.to compute a specified row of Pascal’s triangle  -----##

#An arbitrary row of Pascal’s triangle can be computed 
#by starting with (n0)=1 
#and applying the recurrence relation among binomial coefficients,

def PascalTriangle_row(n):
    PT = {}
    PT0 = [1]
    if n == 0 :
        return PT0
    for n in range(n+1):
        PT[n] = [1]
        for k in range(1, n+1):
            PT[n].append(str(binomial_coeff(n, k)))
    return PT[n]

import math
def binomial_coeff(n, k) :
    if k == n:
        return '1'
    elif k == 1:         
        return str(n)
    elif k > n:          
        return '0'
    else:
        part1 = math.factorial(n)
        part2 = math.factorial(k)
        part3 = math.factorial(n-k)
        return part1 // (part2 * part3)
    
# Test the results
print(PascalTriangle_row(3))    


# In[9]:


def PascalTriangle_rows(n):
    for i in range(1, n+1):
        for j in range(0, n-i+1):
            print(' ', end='')       
        Coeff = 1
        for j in range(1, i+1):
            print(' ', Coeff,sep='',end='')            
           # using Binomial Coefficient
            Coeff = binomial_coeff(i-1, j)
        if i<n or j<n:
            print()
        else:
            return ('')
        
print(PascalTriangle_rows(11))
  


# # Answer to Question 3 - Statistics 101 

# In[23]:


##-----  a. with the Gaussian multiplier -----##

# The standard point and interval estimate for the populaiton mean 
# based on Normal theory takes the form x¯±z×se(x) 
# where x¯ is the mean, se(x) is the standard error, 
# and z is a Gaussian multiplier that depends on the desired confidence level. 
# Write a function to return a point and interval estimate for the mean.

import numpy as np
import scipy.stats as st

def estimate_prob_a(x, c, fmt=None):
    p = x.mean()
    alpha = 1 - c / 100
    serr = x.std(ddof=1) / np.sqrt(x.shape[0])
    z = st.norm.ppf(1 - alpha / 2)
    (lwr, upr) = (p - z * serr, p + z * serr)
    d = {"est": p, "level": c, "lwr": lwr, "upr": upr}
    if fmt is None:
      
        return d
    else:
        return fmt % d


# In[24]:


x.shape[0]


# In[25]:


##-----  b. methods for computing a confidence interval -----##

def estimate_prob_b(x, c, method="Binomial-theory", fmt=None):
    p = x.mean()
    alpha = 1 - c / 100
    if method == "Binomial-theory":
        n = len(x)
        if n * min(p, 1 - p) <= 12:
            print("WARNING")
        serr = np.sqrt(p * (1.0 - p) / n)
        z = st.norm.ppf(1 - alpha / 2)
        (lwr, upr) = (p - z * serr, p + z * serr)
    elif method == "Clopper-Pearson":
        lwr = st.beta.ppf(alpha / 2, x.sum(), len(x) - x.sum() + 1)
        upr = st.beta.ppf(1 - alpha / 2, x.sum() + 1, len(x) - x.sum())
    elif method == "Jeffrey-interval":
        lwr = max(0.0, st.beta.ppf(
            alpha / 2, x.sum() + 0.5, len(x) - x.sum() + 0.5))
        upr = min(
            1.0, st.beta.ppf(1 - alpha / 2, x.sum() +
                             0.5, len(x) - x.sum() + 0.5)
        )
    elif method == "Agresti-Coull":
        p = (x.sum() + 2) / (len(x) + 4)
        serr = np.sqrt(p * (1 - p) / (len(x) + 4))
        z = st.norm.ppf(1 - alpha / 2)
        (lwr, upr) = (p - z * serr, p + z * serr)
    else:
        print("Method not support.")
        return None
    d = {"est": p, "level": c, "lwr": lwr, "upr": upr}
    if fmt is None:
        return d
    else:
        return fmt % d


# In[26]:


##-----  c. methods for computing a confidence interval -----##

def formatstring(point_prec=2, int_prec=4):
    return "%(est).{:d}f[%(level).0f%%CI:(%(lwr).{:d}f, %(upr).{:d}f)]".format(
        point_prec, int_prec, int_prec
    )



def which_method(n):
    if n ==0:
        return 'normal-theory'
    elif n ==1:
        return 'Binomial-theory'
    elif n ==2:
        return 'Clopper-Pearson' 
    elif n ==3:
        return 'Jeffrey-interval'  
    elif n == 4:
        return 'Agresti-Coull'
    else:
        "Wrong method index"

x = [1.0 for i in range(42)]
x.extend([0 for i in range(48)])
x = np.array(x)
# fmtstring = "%(est).2f[%(level).0f%%CI:(%(lwr).4f, %(upr).4f)]"
fmtstring = formatstring(5, 6)

for different_ci in np.array([90, 95, 99]):
    widths = []
    width1s = []
    
    print('When the confidence interval is', different_ci, ":")
    print('--------------------------------------------------------------------' ) 
    print('normal-theory', "|" , estimate_prob_a(x, different_ci, fmtstring))
    width = estimate_prob_a(x, different_ci)['upr'] - estimate_prob_a(x, different_ci)['lwr']

    for m in ["Binomial-theory", "Clopper-Pearson", "Jeffrey-interval", "Agresti-Coull"]:
        print(m,"|" , estimate_prob_b(x, different_ci, m, fmtstring))
        #print(estimate_prob_a(x, different_ci, m)['upr'])
        width1 = estimate_prob_b(x, different_ci, m)['upr'] - estimate_prob_b(x, different_ci, m)['lwr']
        width1s.append(width1)
        
    widths = np.insert(width1s, 0, width)
    widthslist = widths.tolist()
    #widths = np.concatenate((width, width1s.T),axis = 0)
#    print(widths.index(min(widthslist)))
    print('--------------------------------------------------------------------' ) 
    print(which_method(np.argmin(widths, axis=0)), "method produces the interval with the smallest width")    
    
    print('\n')





# In[ ]:




