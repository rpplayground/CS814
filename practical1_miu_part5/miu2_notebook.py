#%% [markdown]
## University of Strathclyde - MSc Artificial Intelligence and Applications
## CS814 - Artificial Intelligence for Autonomous Systems
## Assignment 1 - MIU
# This notebook was first created first created 4th October 2019 by Barry Smart.
#


#%%
import pandas as pd
import numpy as np
import os
import sys

#%%
sys.path

#%%
working_directory = os.getcwd()
#%%
os. chdir(working_directory + "\\practical1_miu_part5")


#%%
from miu2_main import iterate_through_goals

#%%
list_of_goals = [ "MIU", "MIIII", "MUI", "MIIIIUIIIIU", "MIUUIUU", "MIUUIUUIUUIUU", "MIUUIUUIIUU", "MIUUIUUII", "MIUUIUUIIU", "MUUI", "MIIIUI", "MIIUII", "MIUIII", "MUIIII" ]

#%%
results_dataframe = iterate_through_goals(list_of_goals)

# %%
results_dataframe

#%%
