# test_bank.py

from bank import value

def test_hello():
    # Test greetings starting with "hello"
    assert value("hello") == 0
    assert value("Hello there!") == 0
    assert value("HELLO") == 0

def test_h_only():
    # Test greetings starting with "h" but not "hello"
    assert value("hi") == 20
    assert value("Hey there") == 20
    assert value("hola") == 20

def test_other():
    # Test greetings not starting with "h"
    assert value("good morning") == 100
    assert value("Bonjour") == 100
    assert value("Greetings!") == 100
