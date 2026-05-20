import pytest
from src.main import hello

def test_hello():
    assert hello() == "Olá, CodeHealth!"
