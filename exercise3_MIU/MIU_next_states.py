# University of Strathclyde - MSc Artificial Intelligence and Applications
# CS814 - Artificial Intelligence for Autonomous Systems
# Assignment 1 - MUI
# File Created - 1st October 2019 - Barry Smart
# 
# ABOUT:
# This file contains the function that, given a current state, computes next possible states based on a set of 4 rules.
# See body of function for description of each rule.
# The function returns a simple list of possible next states AND a more complex list that rolls up the route to each of those states.

# I've chosen to use regular expressions to test for each of the rules
import re
import numpy as np
import pandas as pd

def next_states(s, route_to_source_from_axiom = []):
    #TODO - check s is a string containing only characters M, I or U.
    list_of_next_states = []
    list_of_next_states_with_route = []
    
    # Define a helper function that will:
    # - check for duplicates;
    # - create route to each state;
    # - appending the given next state(s) to the master lists.
    def remove_duplicates_and_add_route(source, route_to_source, rule_applied, list_of_next_states_from_rule, master_list_of_next_states, master_list_of_next_states_with_route):
        # Check that list has entries
        if len(list_of_next_states_from_rule) > 0:
            # First remove duplicates by using the set function.
            # TODO assumption here is that duplicates won't occur between different rules, only within a rule.
            rule_next_states_deduped =  list(set(list_of_next_states_from_rule))
            
            # Extend the route to the state by adding a new tuple.
            # This creates a list of tuples describing the sequence of rules required to move from axiom to the current state being captured.
            route_tuple = (source, rule_applied)
            route_to_next_state = route_to_source + [route_tuple]
            
            # Now build a list of sub-lists where each sub_list comprises two elements:
            # 1 next state;
            # 2 the route that was taken to achieve that state as defined as a list of tuples
            rule_next_states_with_route = []
            for state in rule_next_states_deduped:
                rule_next_states_with_route.append([state, route_to_next_state])
            # Extend the master lists
            master_list_of_next_states = master_list_of_next_states + rule_next_states_deduped
            master_list_of_next_states_with_route = master_list_of_next_states_with_route + rule_next_states_with_route
            # Return the master lists
        return master_list_of_next_states, master_list_of_next_states_with_route

    # Rule 1
    # Fist rule is that any string ending in an I can have a U added to it:
    # xI -> xIU
    # This rule is singular - ie, if it applies it will only either none or one entry to the agenda.
    # Check if the last character in the current state is an I, if so append a U.
    next_states_rule1 = []
    if s[-1] == "I":
        next_states_rule1.append(s + "U")
        list_of_next_states, list_of_next_states_with_route = remove_duplicates_and_add_route(s, route_to_source_from_axiom, "R1", next_states_rule1, list_of_next_states, list_of_next_states_with_route)

    # Rule 2
    # Second rule is that any string beginning in M can have the remainder of the string "doubled":
    # Mx -> Mxx
    # This rule will always apply assuming that the "axiom" for this will always be MI.
    # Check if the first character is an M, if so "double" the remaining part of the string.
    next_states_rule2 = []
    if s[0] == "M":
        string_to_multiply = s[1:]
        next_states_rule2.append("M" + (2 * string_to_multiply))
        list_of_next_states, list_of_next_states_with_route = remove_duplicates_and_add_route(s, route_to_source_from_axiom, "R2", next_states_rule2, list_of_next_states, list_of_next_states_with_route)
    
    # Rule 3
    # The third rule is that any string with three consecutive I's can be replaced with U:
    # xIIIy -> xUy, where x and/or y can be an empty string
    # This rule potentially returns multiple matches - ie, so it could contribute multiple entries to the agenda.
    length_of_source_state = len(s)
    next_states_rule3 = []
    for index in range (0, length_of_source_state - 2):
        string_to_compare = s[index:index + 3]
        if string_to_compare == "III":
            next_states_rule3.append(s[:index] + "U" + s[index + 3:])
    list_of_next_states, list_of_next_states_with_route = remove_duplicates_and_add_route(s, route_to_source_from_axiom, "R3", next_states_rule3, list_of_next_states, list_of_next_states_with_route)

    # Rule 4
    # The fourth rule is that any two consecutive U's can be deleted:
    # xUUy -> , where x and/or y can be an empty string
    # This rule potentially returns multiple matches - ie, so it could contribute multiple entries to the agenda.
    next_states_rule4 = []
    for index in range (0, length_of_source_state - 1):
        string_to_compare = s[index:index + 2]
        if string_to_compare == "UU":
            next_states_rule4.append(s[:index] + "" + s[index + 2:])
    list_of_next_states, list_of_next_states_with_route = remove_duplicates_and_add_route(s, route_to_source_from_axiom, "R4", next_states_rule4, list_of_next_states, list_of_next_states_with_route)

    return list_of_next_states, list_of_next_states_with_route

