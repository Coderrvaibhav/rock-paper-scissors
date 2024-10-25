from RPS_game import play
from RPS import player

# Example opponent
def random_bot(prev_play, opponent_history=[]):
    return random.choice(["R", "P", "S"])

if __name__ == "__main__":
    player1 = player
    player2 = random_bot  # You can replace this with different bots

    num_games = 1000
    results = play(player1, player2, num_games, verbose=True)

    print(f"Player 1 Score: {results[0]}")
    print(f"Player 2 Score: {results[1]}")
