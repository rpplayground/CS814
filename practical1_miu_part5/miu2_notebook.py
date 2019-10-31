#%% [markdown]
## University of Strathclyde - MSc Artificial Intelligence and Applications
## CS814 - Artificial Intelligence for Autonomous Systems
## Assignment 1 - MIU
# This notebook was first created first created 4th October 2019 by Barry Smart.
#


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
