import random

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
