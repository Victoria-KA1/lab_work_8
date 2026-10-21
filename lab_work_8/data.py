import requests


class DataLayer:
    """Слой данных (Data Layer)."""

    def get_user_data(self, user_id: int) -> dict:
        # Для демонстрации зависимости requests (Задание 2)
        # В реальности здесь был бы requests.get(...)
        try:
            # Просто проверяем, что requests импортирован и работает
            _ = requests.models.Response()
        except Exception:
            pass

        return {"id": user_id, "name": "Виктория", "role": "Студент"}
