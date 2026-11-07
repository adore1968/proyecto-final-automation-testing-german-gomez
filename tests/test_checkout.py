import pytest
from pages import checkout_page
from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage
from utils.logger import logger

@pytest.mark.ui
def test_checkout(usuario_logueado):
  inventory_page = usuario_logueado

  nombre_producto = "Sauce Labs Backpack"

  logger.info(f"Agregando producto: {nombre_producto}")

  inventory_page.agregar_producto_por_nombre(nombre_producto)

  logger.info("Navegando hacia el carrito...")

  inventory_page.navegar_al_carrito()

  cart_page = CartPage(inventory_page.driver)

  logger.info("Navegando hacia el checkout...")

  cart_page.avanzar_checkout()

  checkout_page = CheckoutPage(inventory_page.driver)

  logger.info("Completando el formulario de checkout")

  checkout_page.completar_formulario("German", "Gomez", "1842")

  nombres_productos_checkout = checkout_page.obtener_nombres_productos()

  logger.info("Validando que el producto agregado al carrito exista en el checkout")

  assert nombre_producto in nombres_productos_checkout, f"El producto '{nombre_producto}' no se encuentra en la pagina de checkout"

  subtotal = checkout_page.obtener_subtotal()

  impuestos = checkout_page.obtener_impuestos()

  total = checkout_page.obtener_total()

  logger.info("Validando que la suma del subtotal y de los impuestos coincida con el total")

  assert total == pytest.approx(subtotal + impuestos), "El total no coincide con la suma del subtotal y los impuestos"

  checkout_page.hacer_click_finalizar()

  print("URL actual:", checkout_page.driver.current_url)

  mensaje_confirmacion = checkout_page.obtener_mensaje_confirmacion()

  assert mensaje_confirmacion == "Thank you for your order!", "El mensaje de confirmacion no es el esperado"

  logger.info("El proceso de checkout funciono correctamente!")