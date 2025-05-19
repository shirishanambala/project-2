import tkinter as tk
import random

def play(player_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    player_choice_label.config(text=f"You chose: {player_choice}")
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        result.set("Result: It's a Draw!")
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result.set("Result: You Win!")
    else:
        result.set("Result: You Lose!")

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x300")

title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

player_choice_label = tk.Label(root, text="You chose: ?", font=("Arial", 14))
player_choice_label.pack()

computer_choice_label = tk.Label(root, text="Computer chose: ?", font=("Arial", 14))
computer_choice_label.pack()

result = tk.StringVar()
result.set("Result: Choose Rock, Paper, or Scissors")
result_label = tk.Label(root, textvariable=result, font=("Arial", 14, "bold"), fg="blue")
result_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=15)

for choice in ["Rock", "Paper", "Scissors"]:
    tk.Button(
        button_frame, text=choice, width=10, height=2,
        font=("Arial", 12),
        command=lambda c=choice: play(c)
    ).pack(side=tk.LEFT, padx=10)

root.mainloop()