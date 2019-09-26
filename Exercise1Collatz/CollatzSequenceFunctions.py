# Collatz Function
# First authored by Barry Smart, 26th September 2019

import math

def calculate_length_of_collatz_sequence (n):
    sequence_length = 1
    while (n != 1):
        if (n % 2 == 0):
            n = n // 2
        else:
            n = (3 * n) + 1
        sequence_length = sequence_length + 1
    return sequence_length
    #TO DO : check n is a positive integer?

def find_biggest_sequence(end):
    largest_sequence_length = 1
    largest_sequence_seed = 1
    for m in range(1, end + 1):
        length_of_sequence = calculate_length_of_collatz_sequence(m)
        if (length_of_sequence > largest_sequence_length):
            largest_sequence_length = length_of_sequence
            largest_sequence_seed = m
    print(largest_sequence_seed, largest_sequence_length)
    #TO DO: store result pairs in a dataframe?
    #TO DO: save dataframe to a file for downstream analysis?
    return largest_sequence_seed
        
seed = 100000
result = find_biggest_sequence(seed)

print("The largest result is", result)