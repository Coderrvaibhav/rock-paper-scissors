import random

def player(prev_play, opponent_history=[]):
    if prev_play == "":
        return random.choice(["R", "P", "S"])

    # Example strategy: counter the opponent's last play
    if prev_play == "R":
        return "P"  # Paper beats Rockdef play(player1, player2, num_games, verbose=False):
    player1_score = 0
    player2_score = 0

    for game in range(num_games):
        player1_move = player1("", player2_score)
        player2_move = player2("", player1_score)

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

        if verbose:
            print(f"Game {game + 1}: {player1_move} vs {player2_move} - {result}")

    return player1_score, player2_score

    elif prev_play == "P":
        return "S"  # Scissors beats Paper
    else:
        return "R"  
