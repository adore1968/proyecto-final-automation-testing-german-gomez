import pytest
import requests

BASE_URL = "https://reqres.in/api/users?page=2"

@pytest.mark.api
def test_get_users():
  response = requests.get(BASE_URL)

  assert response.status_code == 200, f"El codigo de estado esperado es 200, pero se obtuvo {response.status_code}"

  data = response.json()

  assert data["page"] == 2, f"Se esperaba la pagina 2, pero se obtuvo {data['page']}"

  assert len(data["data"]) > 0, "No se encontraron usuarios en la respuesta"

CREATE_URL = "https://reqres.in/api/users"

@pytest.mark.api
def test_create_user():
  payload = {"name": "Matias QA", "job": "tester"}

  response = requests.post(CREATE_URL, json=payload)

  assert response.status_code == 201, f"El codigo de estado esperado es 201, pero se obtuvo '{response.status_code}'"

  new_user = response.json()

  assert new_user["name"] == "Matias QA", f"Se esperaba el nombre '{payload['name']}' y se obtuvo '{new_user['name']}'"

  assert "id" in new_user and "createdAt" in new_user, "La respuesta no contiene los campos 'id' y 'createdAt'"

LOGIN_URL = "https://reqres.in/api/login"

@pytest.mark.api
def test_login_successful():
  credenciales = {"email": "eve.holt@reqres.in", "password": "cityslicka"}

  response = requests.post(LOGIN_URL, json=credenciales)

  assert response.status_code == 200

  assert "token" in response.json()

URL = 'https://jsonplaceholder.typicode.com/posts/1'

@pytest.mark.api
def test_delete_post():
  response = requests.delete(URL)

  assert response.status_code == 200

  body = response.json()

  assert body == {} or "id" not in body or body["id"] is None