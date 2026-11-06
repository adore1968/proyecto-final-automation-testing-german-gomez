import pytest
from pages import checkout_page
from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage

@pytest.mark.ui
def test_checkout(usuario_logueado):
  inventory_page = usuario_logueado

  nombre_producto = "Sauce Labs Backpack"

  inventory_page.agregar_producto_por_nombre(nombre_producto)

  inventory_page.navegar_al_carrito()

  cart_page = CartPage(inventory_page.driver)

  cart_page.avanzar_checkout()

  checkout_page = CheckoutPage(inventory_page.driver)

  checkout_page.completar_formulario("German", "Gomez", "1842")

  nombres_productos_checkout = checkout_page.obtener_nombres_productos()

  assert nombre_producto in nombres_productos_checkout, f"El producto '{nombre_producto}' no se encuentra en la pagina de checkout"

  subtotal = checkout_page.obtener_subtotal()

  impuestos = checkout_page.obtener_impuestos()

  total = checkout_page.obtener_total()

  assert total == pytest.approx(subtotal + impuestos), "El total no coincide con la suma del subtotal y los impuestos"

  checkout_page.hacer_click_finalizar()

  print("URL actual:", checkout_page.driver.current_url)

  mensaje_confirmacion = checkout_page.obtener_mensaje_confirmacion()

  assert mensaje_confirmacion == "Thank you for your order!", "El mensaje de confirmacion no es el esperado"