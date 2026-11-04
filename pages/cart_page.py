from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
  # Locators (selectores de elementos)
  _TITLE = (By.CLASS_NAME, "title")
  _CART_ITEMS = (By.CLASS_NAME, "cart_item")
  _INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
  _CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
  _CHECKOUT_BUTTON = (By.ID, "checkout")

  def __init__(self, driver):
    self.driver = driver
    self.wait = WebDriverWait(driver, 10)

  # Metodo para obtener el titulo de la pagina del carrito
  def obtener_titulo(self):
    titulo_elemento = self.wait.until(EC.visibility_of_element_located(self._TITLE))

    return titulo_elemento.text

  # Metodo para obtener la cantidad de productos en el carrito
  def obtener_cantidad_productos(self):
    productos = self.wait.until(EC.presence_of_all_elements_located(self._CART_ITEMS))

    return len(productos)

  # Metodo para obtener los nombres de los productos en el carrito
  def obtener_nombres_productos(self):
    productos = self.wait.until(EC.presence_of_all_elements_located(self._CART_ITEMS))

    nombres_productos = []

    for producto in productos:
      nombre_elemento = producto.find_element(*self._INVENTORY_ITEM_NAME)

      nombres_productos.append(nombre_elemento.text)

    return nombres_productos


  # Metodo para obtener dinamicamente el locator del boton de eliminar un producto por su nombre
  def obtener_locator_remove(self, nombre_producto):
    locator = (By.CSS_SELECTOR, f"button[data-test='remove-{nombre_producto}']")

    return locator
  
  # Metodo para eliminar un producto especifico del carrito por su nombre
  def eliminar_producto(self, nombre_producto):
    locator_remove = self.obtener_locator_remove(nombre_producto)

    boton_eliminar = self.wait.until(EC.element_to_be_clickable(locator_remove))

    boton_eliminar.click()

  # Metodo para hacer click en el boton de continuar comprando
  def continuar_comprando(self):
    boton_continuar = self.wait.until(EC.element_to_be_clickable(self._CONTINUE_SHOPPING_BUTTON))

    boton_continuar.click()

  # Metodo para avanzar al checkout haciendo click en el boton correspondiente
  def avanzar_checkout(self):
    boton_checkout = self.wait.until(EC.element_to_be_clickable(self._CHECKOUT_BUTTON))

    boton_checkout.click()