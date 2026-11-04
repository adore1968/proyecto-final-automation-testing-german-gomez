from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class InventoryPage:
  _TITLE = (By.CLASS_NAME, "title")
  _PRODUCTS = (By.CLASS_NAME, "inventory_item")
  _ADD_BUTTONS = (By.CSS_SELECTOR, "button[data-test*='add-to-cart']")
  _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
  _CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
  _PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
  _ADD_BUTTON = (By.TAG_NAME, "button")

  def __init__(self, driver):
    self.driver = driver
    self.wait = WebDriverWait(driver, 10)

  # Metodo para obtener el titulo de la pagina de inventario
  def obtener_titulo(self):
    titulo_elemento = self.wait.until(EC.visibility_of_element_located(self._TITLE))

    return titulo_elemento.text

  # Metodo para obtener la cantidad de productos en el carrito
  def obtener_contador_carrito(self):
    try:
      badge = self.wait.until(EC.visibility_of_element_located(self._CART_BADGE))
      
      return int(badge.text)
    except TimeoutException:
      return 0
    
  # Metodo para agregar un producto al carrito por su nombre
  def agregar_producto_por_nombre(self, nombre_producto):
    productos = self.wait.until(EC.presence_of_all_elements_located(self._PRODUCTS))

    for producto in productos:
        nombre_elemento = producto.find_element(*self._PRODUCT_NAMES)

        if nombre_elemento.text == nombre_producto:
          boton_agregar = producto.find_element(*self._ADD_BUTTON)

          boton_agregar.click()

          return True

    raise ValueError(f"No se encontro el producto: {nombre_producto}")

  # Metodo para agegar el primer producto disponible al carrito
  def agregar_primer_producto(self):
    primer_boton = self.wait.until(EC.element_to_be_clickable(self._ADD_BUTTONS))

    primer_boton.click()
    return True

  # Metodo para hacer click en el link del carrito
  def navegar_al_carrito(self):
    carrito_link = self.wait.until(EC.element_to_be_clickable(self._CART_LINK))

    carrito_link.click()