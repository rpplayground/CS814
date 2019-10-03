import exercise3_MIU.next_states_function

def test_next_states():
    assert exercise3_MIU.next_states_function.get_next_states("MI") == ["MIU", "MII"]
    assert exercise3_MIU.next_states_function.get_next_states("MIU") == ["MIUIU"]
    assert exercise3_MIU.next_states_function.get_next_states("MII") == ["MIIU", "MIIII"]
