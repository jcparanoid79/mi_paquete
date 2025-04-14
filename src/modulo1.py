# src/mi_paquete/modulo1.py
def saludar(nombre):
  """Saluda a alguien."""
  return f"¡Hola, {nombre}!"

if __name__ == "__main__":
  # Código de prueba para ejecutar directamente
  nombre = input("Introduce tu nombre: ")
  print(saludar(nombre))