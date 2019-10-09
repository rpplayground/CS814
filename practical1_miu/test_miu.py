import pytest
from .miu_next_states import next_states as next_states

def test_level0_1():
    assert next_states("MI") == ["MIU", "MII"]

def test_level1_1():
    assert next_states("MIU") == ["MIUIU"]

def test_level1_2():
    assert next_states("MII") == ["MIIU", "MIIII"]

def test_level2_1():
    assert next_states("MIUIU") == ["MIUIUIUIU"]

def test_level2_2():
    assert next_states("MIIU") == ["MIIUIIU"]

def test_level2_3():
    assert next_states("MIIII") == ["MIIIIU", "MIIIIIIII", "MUI", "MIU"]

def test_level3_1():
    assert next_states("MIUIUIUIU") == ["MIUIUIUIUIUIUIUIU"]

def test_level3_2():
    assert next_states("MIIUIIU") == ["MIIUIIUIIUIIU"]

def test_level3_3():
    assert next_states("MIIIIU") == ["MIIIIUIIIIU", "MUIU", "MIUU"]

def test_level3_4():
    assert next_states("MIIIIIIII") == ["MIIIIIIIIU", "MIIIIIIIIIIIIIIII", "MUIIIII", "MIUIIII", "MIIUIII", "MIIIUII", "MIIIIUI", "MIIIIIU"]

def test_level3_5():
    assert next_states("MUI") == ["MUIU", "MUIUI"]

def test_random1():
    assert next_states("MUUII") == ["MUUIIU", "MUUIIUUII", "MII"]

def test_random2():
    assert next_states("MUUUI") == ["MUUUIU", "MUUUIUUUI", "MUI"]
