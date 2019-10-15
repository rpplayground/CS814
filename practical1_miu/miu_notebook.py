#%% [markdown]
## Assignment 1 - MIU
# This notebook was first created first created 4th October 2019 by Barry Smart.
# 
### Part 1
# 

#%%
import os
current_working_directory = os.getcwd()
current_working_directory

#%%
os.chdir(current_working_directory + "\\practical1_miu")

#%%
from miu_next_states import next_states
from miu_extend_path import extend_path
from miu_breadth_first_search import breadth_first_search

#%% [markdown]
## Next States

#%%
next_states("MI")

#%%
next_states("MII")

#%%
next_states("MIIIIIIII")

#%% [markdown]
## Extend Path

#%%
extend_path(["MI"])

#%%
extend_path(["MI", "MII", "MIIII"])

#%% [markdown]
## Breadth First Search

#%%
breadth_first_search("MUI")

