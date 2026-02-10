import numpy as np
import pandas as pd
import polars as pl

## Exercise 1

# How would you tidy the following data frame 
# so that the rate column is split into cases 
# and population columns?

df = pd.DataFrame({
  "country": ["A","A","B","B","C","C"],
  "year":    [1999, 2000, 1999, 2000, 1999, 2000],
  "rate":    ["0.7K/19M", "2K/20M", "37K/172M", "80K/174M", "212K/1T", "213K/1T"]
})

### Option 1

df.assign(
   counts = lambda d: d.rate.str.split("/").str[0],
   pop = lambda d: d.rate.str.split("/").str[1] 
)

### Option 2

df.assign(
    rate = lambda d: d.rate.str.split("/"),
    counts = pd.col("rate").str[0],
    pop = pd.col("rate").str[1]
).drop(
    "rate", axis=1
)

### Option 3

df.assign(
    rate = lambda d: d.rate.str.split("/")
).explode(
    "rate"
).assign(
    type = lambda d: ["cases", "pop"] * int(len(d)/2)
).pivot(
    index = ["country", "year"],
    columns = "type",
    values = "rate"
).reset_index(
)


## Examples


pl.Series("ints", 
  [1, 2, 3, np.nan], strict = False)
