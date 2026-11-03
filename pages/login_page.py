from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
  URL = "https://www.saucedemo.com/"

  # Locators (selectores de elementos)
  _USER_INPUT = (By.ID, "user-name")
  _USER_PASSWORD = (By.ID, "password")
  _LOGIN_BUTTON = (By.ID, "login-button")
  _ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

  def __init__(self, driver):
    self.driver = driver
    self.wait = WebDriverWait(driver, 10)

  # Metodo para navegar a la pagina de login
  def abrir(self):
    self.driver.get(self.URL)

    return self

  # Metodo para completar el campo de usuario
  def completar_usuario(self, usuario):
    campo = self.wait.until(EC.visibility_of_element_located(self._USER_INPUT))
    
    campo.clear()
    campo.send_keys(usuario)

    return self

  # Metodo para completar el campo de clave
  def completar_clave(self, clave):
    campo = self.wait.until(EC.visibility_of_element_located(self._USER_PASSWORD))

    campo.clear()
    campo.send_keys(clave)

    return self

  # Metodo para hacer click en el boton de login
  def hacer_click_login(self):
    self.wait.until(EC.element_to_be_clickable(self._LOGIN_BUTTON)).click()

    return self

  # Metodo para ejecutar el flujo completo del login
  def completar_login(self, usuario, clave):
    self.completar_usuario(usuario)
    self.completar_clave(clave)
    self.hacer_click_login()

    return self

  # Metodo para verificar si hay un mensaje de error visible
  def esta_error_visible(self):
    try:
      self.wait.until(EC.visibility_of_element_located(self._ERROR_MESSAGE))
      return True
    except:
      return False

  # Metodo para obtener el mensaje de error si es visible
  def obtener_mensaje_error(self):
    if self.esta_error_visible():
      return self.wait.until(EC.visibility_of_element_located(self._ERROR_MESSAGE)).text
    return ""