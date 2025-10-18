from src.app import greet

def test_default():
    assert greet("") == "Hello there, world!"

def test_name():
    assert greet("Caitlin") == "Hello there, Caitlin!"
