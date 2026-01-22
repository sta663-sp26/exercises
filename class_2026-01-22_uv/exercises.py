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

# To make this work we needed to add `from ..data.cleaner import remove_nulls` to `regression.py`

import analytics.models.regression as reg
reg.remove_nulls

# Adding `from ..data.cleaner import remove_nulls` to `__init__.py` is not necessary for this exercise,
# but it would allow you to import remove_nulls directly from analytics.models if desired.

import analytics.models as models
models.remove_nulls


## Exercise 2

```shell
cd calculate_ci
uv init --bare
uv add numpy scipy --no-workspace # this flag is necessary because the exercises folder is already a workspace (this will not typically be needed)
uv run python calculate_ci.py
````