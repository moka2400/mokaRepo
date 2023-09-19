import numpy as np
import pandas as pd

cols = ["fLength", "fWidth", "fSize", "fConc", "fConc1", "fAsym", "fM3Long", "fM3Trans", "fAlpha", "fDist", "class"]
df = pd.read_csv(r"C:\Users\moka\Documents\Datasets\magic+gamma+telescope\magic04.data", names=cols)
print(df.head(10))