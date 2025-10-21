import pytest
from hexorcist import to_decimal, from_decimal 

def test_to_decimal_binary():
    assert to_decimal("1010", 2) == 10
    
def test_to_decimal_hex():
    assert to_decimal("C7", 16) == 199
    
def test_to_decimal_mixed_case():
    assert to_decimal("aF", 16) == 175
    
def test_to_decimal_base8():
    assert to_decimal("175", 8) == 125
    
def test_to_decimal_large_base():
    assert to_decimal("Z", 36) == 35
    
#Now the from_decimal

def test_from_decimal_binary():
    assert from_decimal(10, 2) == "1010"
    
def test_from_decimal_hex(): 
    assert from_decimal(199, 16) == "C7"
    
def test_from_decimal_base8():
    assert from_decimal(125, 8) == "175"
    
def test_from_decimal_large_base():
    assert from_decimal(35, 36) == "Z"
    
def test_from_decimal_zero():
    assert from_decimal(0, 16) == "0"