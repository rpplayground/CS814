# University of Strathclyde
# MSc Artificial Intelligence and Applications
# Barry Smart
# CS814 - Artificial Intelligence for Autonomous Systems
# Exercise 3 - MUI
# File Created - 1st October 2019
# 
# ABOUT:
# This file contains the function that, given a current state, computes next possible states based on a set of 4 rules

# I've chosen to use regular expressions to test for each of the rules
import re

def get_next_states(current_state):
    # First set up the patterns we are trying to match against:
    # Fist rule is that any string ending in an I can have a U added to it
    # xI -> xIU
    pattern_rule_1 = 'I$'
    # Second rule is that any string beginning in M can have the remainder of the string "doubled"
    # Mx -> Mxx
    pattern_rule_2 = '^M'
    # The third rule is that any string with three consecutive I's can be replaced with U - including at the end of the string!
    # xIIIy -> xUy, where y can be an empty string
    pattern_rule_3 = 'III'
    # The fourth rule is that any two consecutive U's can be deleted
    pattern_rule_4 = 'UU'

    # Set up the empty list for the return result
    list_of_next_states = []

    # Test against rule 1
    result_rule_1 = re.findall(pattern_rule_1, current_state)
    number_of_results_1 = len(result_rule_1)
    print('Pattern 1 result:', result_rule_1)
    if number_of_results_1 == 1:
        list_of_next_states.append(current_state + "U")
    elif number_of_results_1 > 1:
        print("Something has gone wrong with rule 1!")

    # Test against rule 2
    result_rule_2 = re.findall(pattern_rule_2, current_state)
    number_of_results_2 = len(result_rule_2)
    print('Pattern 2 result:', result_rule_2)
    if len(result_rule_2) == 1:
        string_to_multiply = re.split(pattern_rule_2, current_state)
        string_to_multiply = list(filter(None, string_to_multiply))[0]
        list_of_next_states.append("M" + (string_to_multiply * 2))
    elif number_of_results_2 > 1:
        print("Something has gone wrong with rule 2!")
    




    # Test against rule 2

    # Test against rule 3

    # Test against rule 4

    # Check for duplicates...

    return list_of_next_states