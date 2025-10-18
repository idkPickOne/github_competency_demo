from src.app import greet

def test_default():
    assert greet("") == "Hello, world!"

def test_name():
    assert greet("Caitlin") == "Hello, Caitlin!"
