# University of Strathclyde - MSc Artificial Intelligence and Applications
# CS814 - Artificial Intelligence for Autonomous Systems
# Assignment 1 - Part 1 - MUI Next States Function
# File Created - 1st October 2019 - Barry Smart
# 
# ABOUT:
# This file contains the function that, when passed a current state s, computes next possible states based on a set of 4 rules.
# See body of function for description of each these four rules.
# The function returns a list of possible next states.
def next_states(s):
    # TODO - check s is a string and that it contains only characters M, I or U.
    # First step is to create empty list. The function will append "next states" to this list as it steps through each of the 4 rules below.
    list_of_next_states = []
    
    # Rule 1
    # Fist rule is that any string ending in an I can have a U added to it:
    # xI -> xIU
    # This rule is singular - ie, if it applies it will only either none or one entry to the agenda.
    # Check if the last character in the current state is an I, if so append a U to the end.
    if s[-1] == "I":
        rule1_result = [s + "U"]
        list_of_next_states = list_of_next_states + rule1_result
    
    # Rule 2
    # Second rule is that any string beginning in M can have the remainder of the string "doubled":
    # Mx -> Mxx
    # This rule will always apply assuming that the "axiom" will always begin with M.
    # Nevertheless I will still check if the first character is an M, and if so "double" the remaining part of the string.
    if s[0] == "M":
        string_to_multiply = s[1:]
        rule2_result = ["M" + (2 * string_to_multiply)]
        list_of_next_states = list_of_next_states + rule2_result
    
    # Rule 3 and 4 need to work with the length of the string passed into the function:
    length_of_source_state = len(s)

    # Rule 3
    # The third rule is that any string with three consecutive I's can be replaced with U:
    # xIIIy -> xUy, where x and/or y can be an empty string
    # This rule potentially returns multiple matches - ie, so it could contribute multiple entries to the agenda.
    rule3_result = []
    for index in range (0, length_of_source_state - 2):
        string_to_compare = s[index:index + 3]
        if string_to_compare == "III":
            rule3_result.append(s[:index] + "U" + s[index + 3:])
    list_of_next_states = list_of_next_states + rule3_result

    # Rule 4
    # The fourth rule is that any two consecutive U's can be deleted:
    # xUUy -> , where x and/or y can be an empty string
    # This rule potentially returns multiple matches - ie, so it could contribute multiple entries to the agenda.
    rule4_result = []
    for index in range (0, length_of_source_state - 1):
        string_to_compare = s[index:index + 2]
        if string_to_compare == "UU":
            rule4_result.append(s[:index] + "" + s[index + 2:])
    # Note - the set() function is being used below will remove any duplicates.
    # The assumption is that duplicates will only occur in the application of each rule 4.
    # TODO - check this assumption?  Discuss at tutorial?
    list_of_next_states = list_of_next_states + list(set(rule4_result))
    
    return list_of_next_states

