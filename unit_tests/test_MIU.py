import pytest
from exercise3_MIU.next_states_function import next_states as next_states

def test_next_states_level0():
    assert next_states("MI") == ["MIU", "MII"]

def test_next_states_level1():
    assert next_states("MIU") == ["MIUIU"]
    assert next_states("MII") == ["MIIU", "MIIII"]

def test_next_states_level2():
    assert next_states("MIUIU") == ["MIUIUIUIU"]
    assert next_states("MIIU") == ["MIIUIIU"]
    assert next_states("MIIII") == ["MIIIIU", "MIIIIIIII", "MUI", "MIU"]

def test_next_states_level3():
    assert next_states("MIUIUIUIU") == ["MIUIUIUIUIUIUIUIU"]
    assert next_states("MIIUIIU") == ["MIIUIIUIIUIIU"]
    assert next_states("MIIIIU") == ["MIIIIUIIIIU", "MUIU", "MIUU"]
    assert next_states("MIIIIIIII") == ["MIIIIIIIIU", "MIIIIIIIIIIIIIIII", "MUIIIII", "MIUIIII", "MIIUIII", "MIIIUII", "MIIIIUI", "MIIIIIU"]
    assert next_states("MUI") == ["MUIU", "MUIUI"]


