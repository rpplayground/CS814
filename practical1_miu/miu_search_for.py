# University of Strathclyde - MSc Artificial Intelligence and Applications
# CS814 - Artificial Intelligence for Autonomous Systems
# Assignment 1 - MUI
# File Created - 4th October 2019 - Barry Smart

# ABOUT:
# This is the main for the MIU assignment.  See:
# - associated notebook for insights into how this performs;
# - assocaited set of pytest unit tests.

from .miu_next_states import next_states

def search_for(theorem, axiom = "MI"):
    #TODO check theorem and axiom are valid strings

    # Seed the agenda, captured here as a list, where each top level item in the list comprises:
    # 1 the name of the element;
    # 2 the route taken to create that element, captured as a list of tuples each formed from two elements:
        # - source element
        # - rule applied
    agenda = [[axiom, []]]

    loop_count = 0

    while loop_count < 100000:
        # Pop the first item off the agenda and unpack it
        next_item_on_agenda = agenda.pop(0)
        # Strip out the state
        state_to_examine = next_item_on_agenda[0]
        # Strip out the route taken to that state
        route_to_state_from_axiom = next_item_on_agenda[1]
        # First task is to check if this state is the goal (theorem) state
        if state_to_examine == theorem:
            break
        else:
            # We calculate the next states and insert them at the end of the agenda
            list_of_next_states, list_of_next_states_with_route = next_states(state_to_examine, route_to_state_from_axiom)
            agenda = agenda + list_of_next_states_with_route
            loop_count = loop_count + 1
    # Calculate the number of steps taken
    number_of_steps = len(route_to_state_from_axiom)
    return axiom, theorem, route_to_state_from_axiom, number_of_steps
