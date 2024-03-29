#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:15:47 2024

@author: naveenchakravarthykoti
"""

import pandas as pd

df = pd.read_csv('/Users/naveenchakravarthykoti/Downloads/filtered_insta_English_new/Combined_new_instagram.csv',engine='python')
 
df1=df[df.ne(df.columns).any(1)]
 
df1.to_csv('/Users/naveenchakravarthykoti/Downloads/filtered_insta_English_new/Total-noextraheader_instagram.csv',index=False)
