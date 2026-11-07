import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def create_driver():
  options = Options()
  options.add_argument("--start-maximized")
  options.add_argument("--disable-features=PasswordLeakDetection")

  # Desactivar funciones del administrador de contraseñas
  options.add_experimental_option(
    "prefs",
    {
      "credentials_enable_service": False,
      "profile.password_manager_enabled": False,
      "profile.password_manager_leak_detection": False
    }
  )

  if os.getenv("CI"):
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

  return webdriver.Chrome(options=options)