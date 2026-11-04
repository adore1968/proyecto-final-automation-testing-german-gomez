import pytest
from utils.data import leer_json_productos
from pages.cart_page import CartPage

PRODUCTOS = leer_json_productos("data/productos.json")

# Test que agrega cada producto del JSON al carrito
@pytest.mark.ui
@pytest.mark.parametrize("producto", PRODUCTOS)
def test_agregar_producto_desde_json(usuario_logueado, producto):
  inventory_page = usuario_logueado

  nombre_producto = producto["nombre"]

  print(f"Agregando producto: {nombre_producto}")

  # Obtener contador inicial del carrito
  contador_inicial = inventory_page.obtener_contador_carrito()

  print(f"Contador inicial: {contador_inicial}")

  # Agregar producto especifico
  inventory_page.agregar_producto_por_nombre(nombre_producto)

  # Verificar que el contador se incremento
  contador_final = inventory_page.obtener_contador_carrito()
  print(f"Contador final: {contador_final}")

  assert contador_final == contador_inicial + 1, f"El contador no se incremento correctamente para {nombre_producto}"

  print("Producto agregado correctamente")

@pytest.mark.ui
def test_verificar_producto_en_carrito(usuario_logueado):
  inventory_page = usuario_logueado

  nombre_producto = "Sauce Labs Backpack"

  inventory_page.agregar_producto_por_nombre(nombre_producto)

  inventory_page.navegar_al_carrito()

  assert "cart.html" in inventory_page.driver.current_url, "No se redirigio al carrito"

  cart_page = CartPage(inventory_page.driver)

  nombres_productos = cart_page.obtener_nombres_productos()

  assert nombre_producto in nombres_productos, f"El producto {nombre_producto} no se encuentra en el carrito"