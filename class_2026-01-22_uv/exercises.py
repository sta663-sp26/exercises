## Exercise 1

# - Use os.chdir() to make sure you're in 
#   `exercises/class_2026-01-22_uv/`
# - Can check with `os.getcwd()`

# 1. Import load_csv from loader.py

from analytics.data.loader import load_csv

# 2. Import both functions from cleaner.py

from analytics.data.cleaner import remove_nulls, normalize

# 3. Import LinearModel with the alias lm

from analytics.models.regression import LinearModel as lm

# 4. From within regression.py, import remove_nulls 
#    using a relative import

import analytics.models.regression as reg
reg.remove_nulls
