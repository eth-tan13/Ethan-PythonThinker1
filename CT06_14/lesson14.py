import random
# print("Hello from lesson 15")

# Task 4

moves = ["scissors", "paper", "stone"]
player_score = 0
computer_score = 0
print("--- Welcome to the Scissors Paper Stone Arena! ---")
while True:
    if computer_score >= 3 or player_score >= 3:
        break
    computer_move = random.choice(moves)
    player_move = input("Pick (1) scissors, (2) paper, or (3) stone: (enter word)\n").lower()
    print(f"Computer move: {computer_move}")
    if player_move not in moves:
        print("Invalid input! Please try again!")
    elif (
        (player_move == "scissors" and computer_move == "paper") or
        (player_move == "paper" and computer_move == "stone") or
        (player_move == "stone" and computer_move == "scissors")
    ):
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1
print(f"Final scores:")
print(f"Player score ({player_score})")
print(f"Computer score ({computer_score})")