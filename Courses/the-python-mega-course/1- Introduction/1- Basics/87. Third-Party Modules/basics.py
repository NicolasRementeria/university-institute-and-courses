# Install third party libraries with pip or pip3, whatever python you are using.

# install pandas library

# pip install pandas

import time
import os
import pandas

while True:
    if os.path.exists("temps_today.csv"):
        data = pandas.read_csv("temps_today.csv")
        print(data.mean())
    else:
        print("File does not exists.")
    time.sleep(10)

# Pandas has an inbuilt mean function that gets you the mean of the values per column

# Output:
# st1    22.125
# st2    20.550
# dtype: float64

data.mean()["st1"]

# Output:

# 22.125

type(data)

# Output:

# <class 'pandas.core.frame.DataFrame'>