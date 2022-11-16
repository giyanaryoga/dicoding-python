import pandas as pd
import numpy as np

dict = {"Negara": ["Indonesia", "Jepang", "Amerika Serikat", "India", "China"], 
        "Ibukota": ["Jakarta", "Tokyo", "Washington, D.C", "New Delhi", "Beijing"],
        "Luas": [1905, 377972, 9834, 3287, 9597],
        "Populas": [264, 143, 1252, 1357, 5298]}

df = pd.DataFrame(dict)

print(df)