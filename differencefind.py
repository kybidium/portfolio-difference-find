import pandas as pd
import numpy as np
import sys

file1 = f'{sys.argv[1]}'
file2 = f'{sys.argv[2]}'

# read each file into dataframe
d_file1 = pd.read_excel(file1)
d_file2 = pd.read_excel(file2)

# retrieve unique values of the issuer names in each file as numpy arrays
file1_uniq = d_file1["Name of Issuer"].unique()
file2_uniq = d_file2["Name of Issuer"].unique()

# store differing items in vars corresponding to each file
file1_items_u = np.setdiff1d(file1_uniq, file2_uniq)
file2_items_u = np.setdiff1d(file2_uniq, file1_uniq)

# print list of items corresponding to each file
print(f"items uniquely in file 1: {[x for x in file1_items_u]}\n")
print(f"items uniquely in file 2: {[x for x in file2_items_u]}")