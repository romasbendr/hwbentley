from .conftest import client


def test_status_ok(client):
	response = client.get("/2")
	assert response.status_code == 200
	

def test_output_1(client):
	response = client.get("/2")
	data = response.data.decode()
	assert data == "1"


def test_output_55(client):
	response = client.get("/10")
	data = response.data.decode()
	assert data == "55"
	

def test_str_status_400(client):
	response = client.get("/asd")
	assert response.status_code == 400


def test_negative_status_400(client):
	response = client.get("/-1")
	assert response.status_code == 400


def test_zero_status_400(client):
	response = client.get("/0")
	assert response.status_code == 200
	

def test_list_status_400(client):
	response = client.get("/['a', '123']")
	assert response.status_code == 400
