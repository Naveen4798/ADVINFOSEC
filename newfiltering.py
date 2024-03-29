#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 17:16:22 2024

@author: naveenchakravarthykoti
"""

import pandas as pd
import os
import re  # Import the re module

input_directory = 'Downloads/english_csv/'
output_directory = 'Downloads/filtered_addi_eng_csv/'

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

verbs = ["remove", "delete", "suspend", "report", "moderate", "block", " raid ", " dox ", "suspend", "harass", " ban "]
nouns = ["user", "account", "content", "tweet", "post", "twitter"]

additional_standalone_keywords = [
    "content moderation", "shadowbanned", "content moderated", "content removed",
    "content deleted", "content shadowbanned", "user moderated", "user removed",
    "user deleted", "user shadowbanned", "account suspended", "account deleted",
    "tweet deleted", "post deleted", "user deleted", "account suspended",
    "remove user", "remove post", "remove tweet", "remove", "remove account",
    "remove content", "user remove", "post remove", "tweet remove", "account remove",
    "content remove", "delete user", "delete post", "delete tweet", "delete",
    "delete account", "delete content", "content delete", "user delete",
    "post delete", "tweet delete", "account delete", "suspend", "suspend user",
    "suspend content", "suspend tweet", "suspend post", "suspend account",
    "account suspend", "suspend tweet", "suspend content", "suspend user",
    "ban user", "ban account", "ban tweet", "ban content", "ban post",
    "account banned", "user banned", "content banned", "tweet banned", "post ban",
    "user ban", "content ban", "tweet ban", "account ban", " dox ", "dox user",
    "user dox", "dox account", "dox twitter", "dox post", "dox tweet",
    "dox content", "tweet dox", "content dox", "post dox", "account dox",
    "twitter dox",
    "harassment", "harassment", "harassment", "harassment", "harass user",
    "user harass", "account harass", "harass account", "harass",
    "harassment",
    # Include all repetitions of "harassment"
]

# Add the provided regex pattern
pattern = (
    r'(?:' + '|'.join(verbs) + r').*?(?:' + '|'.join(nouns) + r')' +
    r'|(?:' + '|'.join(nouns) + r').*?(?:' + '|'.join(verbs) + r')' +
    r'|' + r'(?:' + '|'.join(additional_standalone_keywords) + r')'
)

compiled_pattern = re.compile(pattern, re.IGNORECASE)


def check_relevance(text):
    match = compiled_pattern.search(text)
    if match:
        return True, match.group(0)  # Return matched word
    return False, None


total_tweets_retrieved = 0

for filename in os.listdir(input_directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(input_directory, filename)
        df = pd.read_csv(file_path)
        df['text_lower'] = df['text'].str.lower()
        df['relevant'], df['matched_word'] = zip(*df['text_lower'].apply(check_relevance))  # Unzip matched_word
        filtered_df = df[df['relevant']]
        total_tweets_retrieved += filtered_df.shape[0]
        filtered_df.to_csv(os.path.join(output_directory, f'filtered_{filename}'), index=False)

print(f"Total number of probably relevant tweets retrieved: {total_tweets_retrieved}")
