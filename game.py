human_turn="paper"
computer_turn= "scissors"

if human_turn == "rock" and computer_turn == "scissors":
    print("Human wins!")
if human_turn == "paper" and computer_turn == "rock":
    print("Human wins!")
if human_turn == "scissors" and computer_turn == "paper":
    print("Human wins!")
if human_turn == "rock" and computer_turn == "paper":
    print("Computer wins!")
if human_turn == "paper" and computer_turn == "scissors":
    print("Computer wins!")
if human_turn == "scissors" and computer_turn == "rock":
    print("Computer wins!")
if human_turn == "rock" and computer_turn == "rock":
    print("Draw!")
if human_turn == "paper" and computer_turn == "paper":
    print("Draw!")
if human_turn == "scissors" and computer_turn == "scissors":
    print("Draw!")
