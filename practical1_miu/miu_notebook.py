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

#%%
# axiom, theorem, route_to_state_from_axiom, number_of_steps = search_for("MIIU")
# print("Solution to tranform", axiom, "to", theorem, "can be completed in", number_of_steps, "steps as follows:")
# for i in route_to_state_from_axiom:
#     print("Apply rule", i[1], "to", i[0])


#%%
