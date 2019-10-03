#%% [markdown]
## University of Strathclyde -  MSc Artificial Intelligence and Applications
## CS814 - Artificial Intelligence for Autonomous Systems
## Python Exercise 1 - Collatz Function
# File Created first created 24th September 2019 by Barry Smart.
# 
### Part 1
# This part walks through the examples set out in the XXX.pdf.

#%%
# Import numpy and pandas - we'll use them later on to visualise the results.
import numpy as np
import pandas as pd

#%% [markdown]
#### Create core function
# Create a function that, given a positive integer n, will return the length of the reslt Collatz sequence.

#%%
def calculate_length_of_collatz_sequence (n):
    #TODO : check n is a positive integer?
    sequence_length = 1
    # The assumption is that the sequence will ultimately return to one (unproven)
    #TODO : put some upper limit on the number of iterations the while limit can perform to stop an inifite loop?
    while (n != 1):
        # If n is even...
        if (n % 2 == 0):
            # ... we divide it by 2 
            n = n // 2
        # Otherwise...
        else:
            # ... we multiply it by 3 and add 1
            n = (3 * n) + 1
        # During each successful transition of the while loop, increent the sequence length by 1
        sequence_length = sequence_length + 1
    return sequence_length

#%% [markdown]
#### Create function to iterate and find maximum
# Create a function that steps through positive integers in a definted range and computes the Collatz sequence lenth for each.
# 
# It then returns the maximum Collatz sequence length found, the "seed" that generated that sequence and a list containing all of the pairs to enable visualisation of the result.

#%%
def find_biggest_sequence(starting_integer, ending_integer):
    #TODO check that starting_integer is lower than ending_integer, and both are integers
    # Prime the counters
    largest_sequence_length = 1
    largest_sequence_seed = 1
    result_list = []
    # Step through each of the integers from start to end
    for seed in range(starting_integer, ending_integer + 1):
        # Calculate the length of the Collatz sequence
        length_of_sequence = calculate_length_of_collatz_sequence(seed)
        # If thus is the longest sequence we've seen so far, store it away
        if (length_of_sequence > largest_sequence_length):
            largest_sequence_length = length_of_sequence
            largest_sequence_seed = seed
        result_list.append([seed, length_of_sequence])
    return largest_sequence_seed, largest_sequence_length, result_list

#%%
#### Find largest Collatz sequence between 1 and 100,000
# Call the function to discover the largest sequence length between 1 and 100,000.    
start = 1
end = 100000
seed, length, results = find_biggest_sequence(start, end)
print("The largest Collatz sequence between", start, "and", end, "is", length, "and is generated by", seed, ".")

#%% [markdown]
### Part 2
# Further exploratation of how the Collatz sequence behaves.

#%% [markdown]
#### Function to plot Collatz sequence length over range
# Create a function that will visualise how the Collatz sequence develops as we step through the sequence.

#%%
def plot_collatz(data_frame, max_size):
    # Random sample the results to get something that is more manageable to plot?
    if len(data_frame) > max_size:
        data_frame = data_frame.sample(n=max_size)
    data_frame.plot.scatter(x='seed', y='sequence_length', alpha = 0.2)


#%% [markdown]
#### Exploratory Data Analysis
# Turn the results into a dataframe and set column titles.
# 
# Then Check the data frame that has been created is as expected.

#%%
df = pd.DataFrame(results, columns = ['seed' , 'sequence_length'])
df.head(10)

#%% [markdown]
# Run basic statistics on the "sequence_length"

#%%
df['sequence_length'].describe()

#%% [markdown]
# Visualise the results.  Note - this plot randomly samples 1,000 of the 100,000 data points as the data set is otherwise too slow to plot.

#%%
plot_collatz(df, 1000)

#%% [markdown]
# Now repeat the process to examine how Collatz behaves around the point where the maximum result is returned.   

#%%
start = seed - 500
end = seed + 500
seed, length, results = find_biggest_sequence(start, end)
print("The largest Collatz sequence between", start, "and", end, "is", length, "and is generated by", seed, ".")

#%% [markdown]
# Turn the results into a dataframe, set column titles and plot it.

#%%
df = pd.DataFrame(results, columns = ['seed' , 'sequence_length'])
plot_collatz(df, 1000)

