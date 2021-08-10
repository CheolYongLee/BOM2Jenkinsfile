import pandas as pd
import os

BOMfile = "BOM_20210804.xlsx"

BOM = pd.read_excel(BOMfile, header=None)

print(BOM)