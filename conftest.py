import pytest
from utils.driver import create_driver
import pytest
import pathlib
from datetime import datetime
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import pytest_html

target = pathlib.Path("reports/screens")

target.mkdir(parents=True, exist_ok=True)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
  """Se ejecuta despues de cada fase (setup/call/teardown) de cada test"""
  outcome = yield # Dejamos que Pytest genere el reporte

  report = outcome.get_result() # Obtenemos el objeto report

  # Solo capturamos en fallos de la fase principal
  if report.when == "call" and report.failed:
    driver = item.funcargs.get("driver") # Obtenemos el fixture driver

    if driver:
      fecha_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

      file_name = target / f"{item.name}_{fecha_hora}.png"

      driver.save_screenshot(str(file_name)) # Captura

      if not hasattr(report, "extras"):
        report.extras = []

      report.extras.append(pytest_html.extras.image(str(file_name)))

@pytest.fixture
def driver():
  driver = create_driver()

  yield driver 

  driver.quit()

@pytest.fixture
def usuario_logueado(driver):
  login_page = LoginPage(driver)

  login_page.abrir()

  login_page.completar_login("standard_user", "secret_sauce")

  assert "inventory.html" in driver.current_url

  return InventoryPage(driver)