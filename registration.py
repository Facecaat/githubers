import json


class Register:


    def __init__(self, player):
        self.player = player


    def load_users(self):
        try:
            with open('users.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []


    def dump_users(self, users):
        with open('users.json', 'w', encoding='utf-8') as f:
            json.dump(users, f, ensure_ascii=False)


    def register_player(self):
        users = self.load_users()
        if self.player in users:
            return f"Пользователь '{self.player}' уже зарегистрирован"
        users.append(self.player)
        self.save_users(users)
        return f"Пользователь '{self.player}' успешно зарегистрирован"

    def is_registered(self):
        users = self.load_users()
        if self.player in users:
            return "Пользователь зарегистрирован"
        else:
            return "Пользователь не найден"
