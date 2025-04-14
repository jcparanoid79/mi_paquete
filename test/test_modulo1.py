import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.modulo1 import saludar

def test_saludar_nombre_normal():
    """Test saludar with a regular name"""
    assert saludar("Juan") == "¡Hola, Juan!"

def test_saludar_nombre_vacio():
    """Test saludar with empty string"""
    assert saludar("") == "¡Hola, !"

def test_saludar_nombre_espacios():
    """Test saludar with name containing spaces"""
    assert saludar("Juan Pablo") == "¡Hola, Juan Pablo!"

def test_saludar_nombre_caracteres_especiales():
    """Test saludar with special characters"""
    assert saludar("María#123") == "¡Hola, María#123!"