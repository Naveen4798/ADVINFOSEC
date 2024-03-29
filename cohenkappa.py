#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 12:01:08 2024

@author: naveenchakravarthykoti
"""

'''import pandas as pd
from sklearn.metrics import cohen_kappa_score

# Read the CSV files
file1 = "Desktop/random_2500_twitter1.csv"
file2 = "Desktop/random_2500_twitter.csv"

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Extract the labels from the last column
labels1 = df1['label'].tolist()
labels2 = df2['label'].tolist()

# Ensure both lists have the same length
min_len = min(len(labels1), len(labels2))
labels1 = labels1[:min_len]
labels2 = labels2[:min_len]

# Compute Cohen's Kappa
kappa = cohen_kappa_score(labels1, labels2)

print("Cohen's Kappa:", kappa)'''
import pandas as pd
from sklearn.metrics import confusion_matrix, cohen_kappa_score

# Read the CSV files
file1 = "Downloads/naveen_random_1500-Test_twitter.csv"#naveen
file2 = "Downloads/bharath.csv"#sai

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Extract the labels from the last column
labels1 = df1['label'].tolist()
labels2 = df2['label'].tolist()

# Ensure both lists have the same length
min_len = min(len(labels1), len(labels2))
labels1 = labels1[:min_len]
labels2 = labels2[:min_len]

# Print confusion matrix
conf_matrix = confusion_matrix(labels1, labels2)
print("Confusion Matrix:")
print(conf_matrix)

# Compute Cohen's Kappa
kappa = cohen_kappa_score(labels1, labels2)
print("Cohen's Kappa:", kappa)

