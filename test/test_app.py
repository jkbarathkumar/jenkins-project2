# test_app.py
from main import hello_world
import pytest

def test_hello_world(capfd):
    hello_world()
    captured = capfd.readouterr()
    assert captured.out == "Hello, World!\n"
