#%% [markdown]
## University of Strathclyde - MSc Artificial Intelligence and Applications
## CS814 - Artificial Intelligence for Autonomous Systems
## Practical 1 - MIU
# This notebook was first created first created 4th October 2019 by Barry Smart.
#

#%%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

#%%
os.getcwd()
#%%
os. chdir('c:\\Users\\Barry\\GitHub\\CS814\\practical1_miu')


#%%
from miu_next_states import next_states
from miu_extend_path import extend_path
from miu_breadth_first_search import breadth_first_search
from miu_depth_limited_dfs import depth_limited_dfs
from miu_iterative_deepening import iterative_deepening
from miu_compare_algorithms import compare_algorithms

#%% [markdown]
### Part 1 - Next States
# The following calls illustrate the core "next_states" function working.

#%%
next_states("MI")

#%%
next_states("MII")

#%%
next_states("MIIIIIIII")

#%%
next_states("MUII")

#%% [markdown]
### Part 2 - Extend Path
# The following provide examples of the "extend_paths" function in action.

#%%
extend_path(["MI"])

#%%
extend_path(["MI", "MII", "MIIII"])

#%% [markdown]
## Part 3 - Breadth-First Search
# The following example shows the breadth-first search running with a reasonably challenging goal.
goal = "MUII"

#%%
def print_results(algorithm_name, goal_path, extend_path_counter, agenda_length, maximum_agenda_length):
    print(algorithm_name)
    print("Goal:", goal)
    print("Number of times extend paths called:", extend_path_counter)
    print("Maximum length of agenda:", maximum_agenda_length)
    print("Length of agenda when goal found:", agenda_length)
    print("Path to goal:\n", goal_path)

#%%
goal_path, extend_path_counter, agenda_length, maximum_agenda_length = breadth_first_search(goal)
print_results("Breadth-First Search", goal_path, extend_path_counter, agenda_length, maximum_agenda_length)

#%% [markdown]
## Part 4a - Depth Limited Depth-First Search
# Now running the depth limited DFS algorithm with the same goal as above.
#%%
goal_path, extend_path_counter, agenda_length, maximum_agenda_length = depth_limited_dfs(goal,8)
print_results("Depth Limited Depth-First Search", goal_path, extend_path_counter, agenda_length, maximum_agenda_length)

#%% [markdown]
## Part 4b - Iterative Deepening
# Now running the depth limited DFS algorithm with the same goal as above.
#%%
goal_path, extend_path_counter, agenda_length, maximum_agenda_length = iterative_deepening(goal)
print_results("Iterative Deepening", goal_path, extend_path_counter, agenda_length, maximum_agenda_length)

#%% [markdown]
## Part 4c - Comparing Algorithms
# Now writing a more industrial grade set of functions to allow the different algorithms to be compared.
#%%
comparison_list = compare_algorithms(["MUII", "MIUIUIUIU", "MIIIIUIIIIU", "MUIUI", "MUIIUII", "MIIIII"], 10)

#%%
comparison_dataframe = pd.DataFrame.from_records(comparison_list)

#%%
comparison_dataframe

#%%
# Initialize figure and ax
fig, ax = plt.subplots(figsize=(12,12))
# Set the scale of the y-axes to be a log scale
ax.set(yscale="log")
# Create a regplot
sns.barplot(x="Goal", y="Extend Calls", hue="Algorithm", data=comparison_dataframe, ax=ax)

#%%
fig, ax = plt.subplots(figsize=(12,12))
# Set the scale of the y-axes to be a log scale
ax.set(yscale="log")
# Create a regplot
sns.barplot(x="Goal", y="Max Agenda Length", hue="Algorithm", data=comparison_dataframe, ax=ax)

#%%
fig, ax = plt.subplots(figsize=(12,12))
# Create a regplot
sns.barplot(x="Goal", y="Path Length", hue="Algorithm", data=comparison_dataframe, ax=ax)

#%%
