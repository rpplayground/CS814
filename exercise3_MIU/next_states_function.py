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

def next_states(s, source_level = 0, element_counter = 0):
    #TODO - check s is a string containing only characters M, I or U.
    # Set up the empty list for the return result
    list_of_next_states = []
    list_of_next_states_details = []

    # Rule 1
    # Fist rule is that any string ending in an I can have a U added to it:
    # xI -> xIU
    # This rule is singular - ie, if it applies it will only either none or one entry to the agenda.
    # Check if the last character in the current state is an I, if so append a U
    if s[-1] == "I":
        next_state_rule1 = s + "U"
        list_of_next_states.append(next_state_rule1)
        list_of_next_states_details.append([source_level, element_counter, "R1", next_state_rule1])

    # Rule 2
    # Second rule is that any string beginning in M can have the remainder of the string "doubled":
    # Mx -> Mxx
    # This rule will always apply assuming that the "axiom" for this will always be MI.
    # Check if the first character is an M, if so "double" the remaining part of the string
    if s[0] == "M":
        string_to_multiply = s[1:]
        next_state_rule2 = "M" + (2 * string_to_multiply)
        list_of_next_states.append(next_state_rule2)
        list_of_next_states_details.append([source_level, element_counter, "R2", next_state_rule2])
    
    # Rule 3
    # The third rule is that any string with three consecutive I's can be replaced with U - including at the end of the string!:
    # xIIIy -> xUy, where y can be an empty string
    # This rule potentially returns multiple matches - ie, so it could contribute multiple entries to the agenda.
    start_index = 0
    find_index_list = []
    while s.find('III', start_index) > 0:
        find_index = s.find('III', start_index)
        find_index_list.append(find_index)
        start_index = find_index + 1
    for index in find_index_list:
        start = index
        end = index + 3
        next_state_rule3 = s[:start] + "U" + s[end:]
        list_of_next_states.append(next_state_rule3)
        list_of_next_states_details.append([source_level, element_counter, "R3", next_state_rule3])

    # Rule 4
    # The fourth rule is that any two consecutive U's can be deleted
    # xUUy -> xy
    start_index = 0
    find_index_list = []
    while s.find('UU', start_index) > 0:
        find_index = s.find('UU', start_index)
        find_index_list.append(find_index)
        start_index = find_index + 1
    for index in find_index_list:
        start = index
        end = index + 3
        next_state_rule3 = s[:start] + "" + s[end:]
        list_of_next_states.append(next_state_rule3)
        list_of_next_states_details.append([source_level, element_counter, "R3", next_state_rule3])
    
    # Check for duplicates...

    return list_of_next_states, list_of_next_states_details

next_states("MIIII")