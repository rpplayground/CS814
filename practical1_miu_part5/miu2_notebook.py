#%%
import pandas as pd
import numpy as np
from miu2_main import iterate_through_goals

#%%
list_of_goals = [ "MIU", "MIIII", "MUI", "MIIIIUIIIIU", "MIUUIIIIU", "MIUUIUU", "MIUUIUUIUUIUU", "MIUUIUUIIUU", "MIUUIUUII", "MIUUIUUIIU" ]

#%%
results_dataframe = iterate_through_goals(list_of_goals)

# %%
print(results_dataframe)

#%%
