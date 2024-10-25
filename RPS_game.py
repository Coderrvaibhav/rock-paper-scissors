import random

# Player function
def player(prev_play, opponent_history=[]):
    if prev_play == "":
        return random.choice(["R", "P", "S"])

    # Example strategy: counter the opponent's last play
    if prev_play == "R":
        return "P"  # Paper beats Rock
    elif prev_play == "P":
        return "S"  # Scissors beats Paper
    else:
        return "R"  # Rock beats Scissors

# Play function
def play(player1, player2, num_games, verbose=False):
    player1_score = 0
    player2_score = 0
    opponent1_history = []  # Track opponent 1 history
    opponent2_history = []  # Track opponent 2 history

    for game in range(num_games):
        player1_move = player1(opponent2_history[-1] if opponent2_history else "")
        player2_move = player2(opponent1_history[-1] if opponent1_history else "")

        if player1_move == player2_move:
            result = "Tie"
        elif (player1_move == "R" and player2_move == "S") or \
             (player1_move == "P" and player2_move == "R") or \
             (player1_move == "S" and player2_move == "P"):
            result = "Player 1 wins"
            player1_score += 1
        else:
            result = "Player 2 wins"
            player2_score += 1

        # Update opponent history
        opponent1_history.append(player1_move)
        opponent2_history.append(player2_move)

        if verbose:
            print(f"Game {game + 1}: {player1_move} vs {player2_move} - {result}")

    return player1_score, player2_score

# Example usage:
# player1_score, player2_score = play(player, another_player_function, 1000, verbose=True)
