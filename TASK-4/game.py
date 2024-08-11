import random
import tkinter as tk
from tkinter import messagebox
# Initialize the score table
score_table = {"User": 0, "Computer": 0, "Ties": 0}
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "User"
    else:
        return "Computer"
def update_score(winner):
    if winner == "User":
        score_table["User"] += 1
    elif winner == "Computer":
        score_table["Computer"] += 1
    else:
        score_table["Ties"] += 1
def display_score():
    for widget in score_frame.winfo_children():
        widget.destroy()  
    tk.Label(score_frame, text="User", borderwidth=2, relief="groove").grid(row=0, column=0, sticky="nsew")
    tk.Label(score_frame, text="Computer", borderwidth=2, relief="groove").grid(row=0, column=1, sticky="nsew")
    tk.Label(score_frame, text="Ties", borderwidth=2, relief="groove").grid(row=0, column=2, sticky="nsew") 
    tk.Label(score_frame, text=score_table["User"], borderwidth=2, relief="groove").grid(row=1, column=0, sticky="nsew")
    tk.Label(score_frame, text=score_table["Computer"], borderwidth=2, relief="groove").grid(row=1, column=1, sticky="nsew")
    tk.Label(score_frame, text=score_table["Ties"], borderwidth=2, relief="groove").grid(row=1, column=2, sticky="nsew")
def play(user_choice):
    computer_choice = get_computer_choice()
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")   
    winner = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Result: {winner}")    
    update_score(winner)
    display_score()
def stop_game():
    if score_table["User"] > score_table["Computer"]:
        final_winner = "User"
    elif score_table["User"] < score_table["Computer"]:
        final_winner = "Computer"
    else:
        final_winner = "Tie"
    messagebox.showinfo("Game Over", f"The final winner is: {final_winner}")
    root.destroy()
# Initialize the GUI
root = tk.Tk()
root.title("Rock, Paper, Scissors")
# Create widgets
rock_button = tk.Button(root, text="Rock", command=lambda: play("rock"))
paper_button = tk.Button(root, text="Paper", command=lambda: play("paper"))
scissors_button = tk.Button(root, text="Scissors", command=lambda: play("scissors"))
stop_button = tk.Button(root, text="Stop", command=stop_game)
computer_choice_label = tk.Label(root, text="Computer chose: ")
result_label = tk.Label(root, text="Result: ")
# Create a frame for the score table
score_frame = tk.Frame(root, borderwidth=2, relief="groove")
# Place widgets using grid layout
rock_button.grid(row=0, column=0, padx=10, pady=10)
paper_button.grid(row=0, column=1, padx=10, pady=10)
scissors_button.grid(row=0, column=2, padx=10, pady=10)
stop_button.grid(row=0, column=3, padx=10, pady=10)
computer_choice_label.grid(row=1, column=0, columnspan=4)
result_label.grid(row=2, column=0, columnspan=4)
score_frame.grid(row=3, column=0, columnspan=4, pady=10)
stop_button.grid(row=4, column=0, columnspan=4, pady=10)
# Initial display of the score table
display_score()
# Run the main loop
root.mainloop()
