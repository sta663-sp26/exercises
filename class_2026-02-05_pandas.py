import pandas as pd
import numpy as np


n = 5
d = {
  "id":     np.random.randint(100, 999, n),
  "weight": np.random.normal(70, 20, n),
  "height": np.random.normal(170, 15, n),
  "date":   pd.date_range(start='2/1/2026', periods=n, freq='D')
}

pd.DataFrame(d)
