"""
このファイルに解答コードを書いてください
"""

import pandas as pd
import numpy as np

data_df = pd.read_csv("input.txt", header=None, sep=":")
m     = int(data_df.values[-1, 0])
i_seq = data_df.values[:-1, 0].astype(int)
s_seq = data_df.values[:-1, 1]

def print_str(m, i_seq, s_seq): 
    i_cands = []
    iv_cands = []

    for i, iv in enumerate(i_seq):
        if m%iv==0:
            i_cands.append(i)
            iv_cands.append(iv)

    if len(i_cands)==0:
        print(m)
        return False
    iv_cands = np.array(iv_cands)
    i_cands  = np.array(i_cands)
    i_sorted = np.argsort(iv_cands).astype(int)
    printed  = s_seq[i_cands[i_sorted]]

    for s in printed:
        print(s, end="")
    return True

print_str(m, i_seq, s_seq)
