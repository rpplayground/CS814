#%% [markdown]
## Assignment 1 - MIU
# This notebook was first created first created 4th October 2019 by Barry Smart.
# 
### Part 1
# 

#%%
from practical1_miu.miu_next_states import next_states
from practical1_miu.miu_search_for import search_for

#%%
next_states("MI")

#%%
next_states("MII")

#%%
next_states("MIIIIIIII")

#%%
axiom, theorem, route_to_state_from_axiom, number_of_steps = search_for("MIIU")
print("Solution to tranform", axiom, "to", theorem, "can be completed in", number_of_steps, "steps as follows:")
for i in route_to_state_from_axiom:
    print("Apply rule", i[1], "to", i[0])


#%%
