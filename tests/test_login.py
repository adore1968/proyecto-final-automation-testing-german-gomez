from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import pytest
from utils.data import leer_csv_login
from utils.logger import logger

CASOS_LOGIN = leer_csv_login("data/login.csv")

# Test parametrizado que verifica el login con datos del CSV
@pytest.mark.ui
@pytest.mark.parametrize("usuario, clave, descripcion, debe_funcionar", CASOS_LOGIN)
def test_login(driver, usuario, clave, descripcion, debe_funcionar):
  logger.info(f"Iniciando login con usuario: {usuario}")

  # Paso 1: Abrir pagina de Login
  login_page = LoginPage(driver)

  login_page.abrir()

  # Paso 2: Completar credenciales
  logger.info("Completando credenciales...")
  login_page.completar_login(usuario, clave)

  # Paso 3: Validar resultado
  if debe_funcionar:
    # Login exitoso: debe llegar al inventario
    logger.info("Verificando redireccion exitosa")

    assert "inventory.html" in driver.current_url, f"Login fallo para {usuario}"

    inventory_page = InventoryPage(driver)

    titulo = inventory_page.obtener_titulo()

    assert titulo == "Products", f"Titulo incorrecto: {titulo}"

    logger.info("Test de login completado exitosamente")
  else:
    # Login fallido: debe mostrar error
    assert login_page.esta_error_visible(), f"No se mostro error para {usuario}"

    mensaje_error = login_page.obtener_mensaje_error()

    assert len(mensaje_error) > 0, "El mensaje de error esta vacio"

    logger.info("Login fallo correctamente")