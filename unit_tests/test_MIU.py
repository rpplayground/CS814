import exercise3_MIU.next_states_function

def test_next_states():
    # Level 0
    assert exercise3_MIU.next_states_function.next_states("MI") == ["MIU", "MII"]
    # Level 1
    assert exercise3_MIU.next_states_function.next_states("MIU") == ["MIUIU"]
    assert exercise3_MIU.next_states_function.next_states("MII") == ["MIIU", "MIIII"]
    # Level 2
    assert exercise3_MIU.next_states_function.next_states("MIUIU") == ["MIUIUIUIU"]
    assert exercise3_MIU.next_states_function.next_states("MIIU") == ["MIIUIIU"]
    assert exercise3_MIU.next_states_function.next_states("MIIII") == ["MIIIIU", "MIIIIIIII", "MUI", "MIU"]
    # Level 3
    assert exercise3_MIU.next_states_function.next_states("MIUIUIUIU") == ["MIUIUIUIUIUIUIUIU"]
    assert exercise3_MIU.next_states_function.next_states("MIIUIIU") == ["MIIUIIUIIUIIU"]
    assert exercise3_MIU.next_states_function.next_states("MIIIIU") == ["MIIIIUIIIIU", "MUIU", "MIUU"]
    assert exercise3_MIU.next_states_function.next_states("MIIIIIIII") == ["MIIIIIIIIU", "MIIIIIIIIIIIIIIII", "MUIIIII", "MIUIIII", "MIIUIII", "MIIIUII", "MIIIIUI"]
    assert exercise3_MIU.next_states_function.next_states("MUI") == ["MUIU", "MUIUI"]
    # The following is a duplicate test
    # assert exercise3_MIU.next_states_function.get_next_states("MIU") == ["MIUIU"]
