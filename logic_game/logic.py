class LogicGame:
    def start_game(selfg):
        while True:
            print("Welcome to Logic Game")
            player1 = input("Player 1 name: ")
            player2 = input("Player 2 name: ")
            if player2[-1] == player1[-1]:
                continue

            if player1[-1] == player2[-1]:
                continue

            if player2[-1] != player1[-1]:
                print("Player 1 fuck your ass!")
                break

            if player1[-1] != player2[-1]:
                print("Player 2 fuck your ass!")
                break

            if player2 == player1:
                print("Такое слово уже было")

            if player1 == player2:
                print("Такое слово уже было")
