import pytest
import pathlib

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
      file_name = target / f"{item.name}.png"

      driver.save_screenshot(str(file_name)) # Captura

      if hasattr(report, "extra"):
        report.extra.append({"name": "screenshot", "format": "image", "content": str(file_name)})