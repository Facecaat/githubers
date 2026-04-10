class GameLogic:
    first_player_command = ""
    second_player_command = ""
    stop_commands = ["exit", "stop"]

    @staticmethod
    def start_game(first_player: str, second_player: str):
        while True:
            if GameLogic.first_player_command not in GameLogic.stop_commands and GameLogic.second_player_command not in GameLogic.stop_commands:
