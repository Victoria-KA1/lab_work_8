from lab_work_8.data import DataLayer


class UserService:
    """Слой сервисов (Service Layer)."""

    def __init__(self):
        self.data_layer = DataLayer()

    def get_user_greeting(self, user_id: int) -> str:
        user = self.data_layer.get_user_data(user_id)
        return f"Привет, {user['name']}! Твоя роль: {user['role']}."
