import json


class Register:

    @staticmethod
    def load_users():
        try:
            with open('users.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    @staticmethod
    def dump_users(users):
        with open('users.json', 'w', encoding='utf-8') as f:
            json.dump(users, f, ensure_ascii=False)

    @staticmethod
    def register_player(nickname: str):
        users = Register.load_users()
        if nickname in users:
            return f"Пользователь '{nickname}' уже зарегистрирован"
        users.append(nickname)
        Register.dump_users(users)
        return f"Пользователь '{nickname}' успешно зарегистрирован"

    @staticmethod
    def is_registered(nickname: str):
        users = Register.load_users()
        if nickname in users:
            return True
        return False
