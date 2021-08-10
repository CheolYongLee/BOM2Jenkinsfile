import pandas as pd
import os

BOMfile = "BOM_20210804.xlsx"

BOM = pd.read_excel(BOMfile, header=None)

ver = BOM[1][0]
data = BOM[1][1]
Author = BOM[1][2]

try:
    column = 5
    list_ID = []
    while column >= 5 and BOM[1][column]:
        list_ID.append(str(BOM[1][column]))
        column += 1
except (ValueError, KeyError):
    pass
print(list_ID)

try:
    column = 5
    list_ver = []
    while column >= 5 and BOM[2][column]:
        list_ver.append(str(BOM[2][column]))
        column += 1
except (ValueError, KeyError):
    pass
print(list_ver)