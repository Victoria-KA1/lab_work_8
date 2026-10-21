import argparse

from lab_work_8.service import UserService


def main():
    parser = argparse.ArgumentParser(description="Моя CLI утилита")
    parser.add_argument("user_id", type=int, help="ID пользователя")
    args = parser.parse_args()

    service = UserService()
    result = service.get_user_greeting(args.user_id)
    print(result)


if __name__ == "__main__":
    main()
