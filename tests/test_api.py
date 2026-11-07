import pytest
import requests
from utils.logger import logger

@pytest.mark.api
def test_get_users(get_url):
  logger.info("Probando una peticion GET con requests")

  url = get_url

  response = requests.get(url)

  assert response.status_code == 200, f"El codigo de estado esperado es 200, pero se obtuvo {response.status_code}"

  logger.info("El codigo de estado es el esperado")

  data = response.json()

  assert data["page"] == 2, f"Se esperaba la pagina 2, pero se obtuvo {data['page']}"

  assert len(data["data"]) > 0, "No se encontraron usuarios en la respuesta"

  logger.info("Los usuarios devueltos son de la pagina 2 y hay por lo menos un usuario")

@pytest.mark.api
def test_create_user(post_url):
  logger.info("Probando una peticion POST con requests")

  url = post_url

  payload = {"name": "Matias QA", "job": "tester"}

  response = requests.post(url, json=payload)

  assert response.status_code == 201, f"El codigo de estado esperado es 201, pero se obtuvo '{response.status_code}'"

  logger.info("El codigo de estado es el esperado")

  new_user = response.json()

  assert new_user["name"] == "Matias QA", f"Se esperaba el nombre '{payload['name']}' y se obtuvo '{new_user['name']}'"

  logger.info("Los datos creados coinciden con los devueltos")

  assert "id" in new_user and "createdAt" in new_user, "La respuesta no contiene los campos 'id' y 'createdAt'"

  logger.info("Propiedades como 'id' y 'createdAt' existen en el objeto devuelto por la API")

@pytest.mark.api
def test_login_successful(login_url):
  logger.info("Probando una peticion POST con requests en el contexto de un login exitoso")

  url = login_url

  credenciales = {"email": "eve.holt@reqres.in", "password": "cityslicka"}

  response = requests.post(url, json=credenciales)

  assert response.status_code == 200

  assert "token" in response.json()

  logger.info("El login fue exitoso, el codigo de estado y la propiedad 'token' conciciden")

@pytest.mark.api
def test_login_unsuccessful(login_url):
  logger.info("Probando una peticion POST con requests en el contexto de un login fallido")

  url = login_url

  credenciales = {"email": "eve.holt@reqres.in"}

  response = requests.post(url, json=credenciales)

  assert response.status_code == 400

  assert "error" in response.json()

  logger.info("El login fue fallido correctamente, el codigo de estado y la propiedad 'error' conciciden")

@pytest.mark.api
def test_delete_post(delete_by_id_url):
  logger.info("Probando una peticion DELETE con requests de manera dinamica por su id")

  url = delete_by_id_url(1)

  response = requests.delete(url)

  assert response.status_code == 200

  body = response.json()

  assert body == {} or "id" not in body or body["id"] is None

  logger.info("La peticion DELETE fue correcta, codigo de estado y la ausencia de un body coinciden con lo esperado")