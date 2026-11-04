from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
  # Locators
  _TITLE = (By.CLASS_NAME, "title")
  _FIRST_NAME = (By.ID, "first-name")
  _LAST_NAME = (By.ID, "last-name")
  _POSTAL_CODE = (By.ID, "postal-code")
  _CONTINUE_BUTTON = (By.ID, "continue")

  _CART_ITEM = (By.CLASS_NAME, "cart_item")
  _INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
  _SUBTOTAL = (By.CLASS_NAME, "summary_subtotal_label")
  _TAX = (By.CLASS_NAME, "summary_tax_label")
  _TOTAL = (By.CLASS_NAME, "summary_total_label")
  _FINISH_BUTTON = (By.ID, "finish")

  def __init__(self, driver):
    self.driver = driver
    self.wait = WebDriverWait(driver, 10)

  # Metodo para obtener el titulo de la pagina de checkout
  def obtener_titulo(self):
    titulo_elemento = self.wait.until(EC.visibility_of_element_located(self._TITLE))

    return titulo_elemento.text

  # Metodo para completar el campo de nombre
  def completar_nombre(self, nombre):
    nombre_input = self.wait.until(EC.visibility_of_element_located(self._FIRST_NAME))

    nombre_input.clear()

    nombre_input.send_keys(nombre)

    
  # Metodo para completar el campo de apellido
  def completar_apellido(self, apellido):
    apellido_input = self.wait.until(EC.visibility_of_element_located(self._LAST_NAME))

    apellido_input.clear()

    apellido_input.send_keys(apellido)

  # Metodo para completar el campo de codigo postal
  def completar_codigo_postal(self, codigo_postal):
    codigo_postal_input = self.wait.until(EC.visibility_of_element_located(self._POSTAL_CODE))

    codigo_postal_input.clear()

    codigo_postal_input.send_keys(codigo_postal)

  # Metodo para hacer click en el boton de continuar
  def hacer_click_continuar(self):
    continuar_boton = self.wait.until(EC.element_to_be_clickable(self._CONTINUE_BUTTON))

    continuar_boton.click()

  # Metodo para completar el formulario de checkout
  def completar_formulario(self, nombre, apellido, codigo_postal):
    self.completar_nombre(nombre)

    self.completar_apellido(apellido)

    self.completar_codigo_postal(codigo_postal)

    self.hacer_click_continuar()

