import pytest
from .miu_next_states import next_states as next_states

def test_next_states_from_list():
    test_list = [["MI", ["MIU", "MII"]], ["MIU", ["MIUIU"]], ["MII", ["MIIU", "MIIII"]]]
    for item in test_list:
        assert set(next_states(item[0])[0]) == set(item[1])

def test_next_states_level0():
    assert next_states("MI")[0] == ["MIU", "MII"]

def test_next_states_level1():
    assert next_states("MIU")[0] == ["MIUIU"]
    assert next_states("MII")[0] == ["MIIU", "MIIII"]

def test_next_states_level2():
    assert next_states("MIUIU")[0] == ["MIUIUIUIU"]
    assert next_states("MIIU")[0] == ["MIIUIIU"]
    assert set(next_states("MIIII")[0]) == set(["MIIIIU", "MIIIIIIII", "MUI", "MIU"])

def test_next_states_level3_0():
    assert next_states("MIUIUIUIU")[0] == ["MIUIUIUIUIUIUIUIU"]

def test_next_states_level3_1():
    assert next_states("MIIUIIU")[0] == ["MIIUIIUIIUIIU"]
    assert next_states("MIIIIU")[0] == ["MIIIIUIIIIU", "MUIU", "MIUU"]
    assert next_states("MIIIIIIII")[0] == ["MIIIIIIIIU", "MIIIIIIIIIIIIIIII", "MUIIIII", "MIUIIII", "MIIUIII", "MIIIUII", "MIIIIUI", "MIIIIIU"]
    assert next_states("MUI")[0] == ["MUIU", "MUIUI"]


