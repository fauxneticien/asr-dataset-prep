
import pandas as pd
import unicodedata

from collections import Counter
from tqdm.contrib.concurrent import process_map

class CharSetExplorer:
    
    def get_vocab(self, texts_list, ids_list):
        
        def sum_counters(counter_list):
            if len(counter_list) > 10:
                counter_0 = sum_counters(counter_list[:int(len(counter_list)/2)])
                counter_1 = sum_counters(counter_list[int(len(counter_list)/2):])
                return sum([counter_0, counter_1], Counter())
            else:
                return sum(counter_list, Counter())
            
        char_counts = process_map(Counter, texts_list, chunksize=1000, ncols=100)
        
        text_char_df = pd.concat([
            pd.DataFrame({ 'id' : ids_list, 'text' : texts_list }),
            pd.DataFrame(char_counts).fillna(0).astype(int)
        ], axis=1)
        
        char_aggs = sum_counters(char_counts)
        
        return char_aggs, text_char_df
    
    def __init__(self, texts_df, text_col, id_col):
        self.texts_df = texts_df
        self.text_col = text_col
        self.id_col = id_col

        self.raw_chars_unique, self.raw_chars_df = self.get_vocab(texts_df[text_col].to_list(), texts_df[id_col].to_list())

    def print_charset(self, with_descriptions=False, expected_charset=None):
        
        def get_unicode_name_gracefully(char):
            try:
              char_name = unicodedata.name(char)
            except:
              char_name = 'NA'

            return char_name

        raw_chars = sorted(self.raw_chars_unique.keys())

        if with_descriptions:
            print(f"There are {len(raw_chars)} unique characters in the raw text (Column number of raw_chars_df: Character, No. of occurrences):\n")
            print(", ".join([ f"({i}: '{c}', {get_unicode_name_gracefully(c)})" for (i,c) in enumerate(self.raw_chars_df.columns) if c not in ['id', 'text'] ]))
        else:
            print(f"There are {len(raw_chars)} unique characters in the raw text (Column number of raw_chars_df: Character, Description):\n")
            print(", ".join([ f"({i}: '{c}', {self.raw_chars_unique[c]})" for (i,c) in enumerate(self.raw_chars_df.columns) if c not in ['id', 'text'] ]))

        if expected_charset != None:
            print("\n")
            print("The following do not appear in the expected charset:")
            print(", ".join([ f"({i}: '{c}', {self.raw_chars_unique[c]})" for (i,c) in enumerate(self.raw_chars_df.columns) if c not in ['id', 'text'] and c not in expected_charset ]))

    def show_texts_with_chars(self, char_col_ids):
        df = self.raw_chars_df
        return df[(df.iloc[:,char_col_ids] > 0).any(axis=1)].iloc[:, [0, 1] + char_col_ids]
