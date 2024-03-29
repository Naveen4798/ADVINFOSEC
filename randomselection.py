#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 14:15:56 2024

@author: naveenchakravarthykoti
"""

import pandas as pd
import random


input_csv_path = 'Downloads/filtered_addi_eng_new_csv/Total-noextraheader_twitter.csv'
output_csv_path = 'Downloads/filtered_addi_eng_new_csv/random_2500_twitter_label.csv'

num_rows_to_select = 2500

df = pd.read_csv(input_csv_path)

if len(df) <= num_rows_to_select:
    print("Error: The input CSV file does not have enough rows.")
else:
    random_rows = df.sample(n=num_rows_to_select, random_state=47)  # You can change the random_state for different randomization

    random_rows.to_csv(output_csv_path, index=False)

    print(f"Random {num_rows_to_select} rows saved to {output_csv_path}")
