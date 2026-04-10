import os

class Registry:
    FILE_NAME = "players.txt"

    def __init__(self):
        if not os.path.exists(Registry.FILE_NAME):
            with open(Registry.FILE_NAME, "w", encoding="utf-8"):
                pass

    @staticmethod
    def registry_player(player_name: str):
        with open(Registry.FILE_NAME, "a", encoding="utf-8") as file:
            file.write(player_name+'\n')

    @staticmethod
    def show_players():
        with open(Registry.FILE_NAME, "r", encoding="utf-8") as file:
            return file.readlines()

registry = Registry()
registry.registry_player(input())
registry.show_players()
registry.registry_player(input())
registry.show_players()
