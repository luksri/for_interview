from fastapi.testclient import TestClient
import httpx
import pytest
from fast_api_ex import app, get_external_data, get_message, ExternalService
from unittest.mock import patch, MagicMock, AsyncMock

client = TestClient(app)
mock_db = MagicMock()

# Mocking function test
@pytest.mark.parametrize("mock_response",[{'message':'mock data'}])
def test_mock_get_data(mock_response):
    with patch("fast_api_ex.get_data", return_value=mock_response):
        response = client.get("/data")
        assert response.status_code == 200
        assert response.json() == mock_response

## mocking a varaiable
@pytest.mark.parametrize('mock_config',['new value'])
def test_mock_variable(mock_config):
    with patch('fast_api_ex.config_val', mock_config):
        response = client.get("/config")
        assert response.status_code == 200
        assert response.json() == {'config':mock_config}

def test_mock_database():
    with patch("fast_api_ex.get_db", return_value=mock_db):
        response = client.get("/items/")
        assert response.status_code == 200

def test_api_response():
    mock_response = {'data': "mocked api response"}
    with patch("httpx.get", return_value=MagicMock(json=lambda:mock_response)):
        assert get_external_data() == mock_response

@pytest.mark.asyncio
async def test_mock_async_function():
    with patch("fast_api_ex.get_message", new_callable=AsyncMock, return_value={"msg": "Mocked Async Data"}):
        assert await get_message() == {"msg": "Mocked Async Data"}

## patching class objects
def test_mock_class_methods():
    with patch.object(ExternalService, "fetch_data", return_value="mocked class function value"):
        service = ExternalService()
        assert service.fetch_data() == "mocked class function value"