from lab_work_8.service import UserService
from lab_work_8.data import DataLayer


def test_data_layer_returns_dict():
    """Тест слоя данных."""
    data_layer = DataLayer()
    result = data_layer.get_user_data(1)
    assert isinstance(result, dict)
    assert result["id"] == 1


def test_service_layer_greeting():
    """Тест слоя сервисов."""
    service = UserService()
    greeting = service.get_user_greeting(42)
    assert "Привет, Виктория!" in greeting
    assert "Студент" in greeting
