import tkinter as tk
from tkinter import messagebox

def start_game(mode):
    window.destroy()
    if mode == "human":
        game_with_human()
    elif mode == "computer":
        game_with_computer()

def game_with_human():
    def check_winner():
        for row in board:
            if row[0] == row[1] == row[2] != "":
                return True
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != "":
                return True
        if board[0][0] == board[1][1] == board[2][2] != "":
            return True
        if board[0][2] == board[1][1] == board[2][0] != "":
            return True
        return False

    def check_draw():
        for row in board:
            if "" in row:
                return False
        return True

    def button_click(row, col):
        nonlocal current_player

        if board[row][col] == "":
            board[row][col] = current_player
            buttons[row][col].config(text=current_player)

            if check_winner():
                messagebox.showinfo("Победа!", f"Игрок {current_player} выиграл!")
                reset_game()
            elif check_draw():
                messagebox.showinfo("Ничья", "Игра закончилась вничью!")
                reset_game()
            else:
                current_player = "O" if current_player == "X" else "X"
                status_label.config(text=f"Ход игрока: {current_player}")

    def reset_game():
        nonlocal board, current_player
        board = [["", "", ""], ["", "", ""], ["", "", ""]]
        current_player = "X"
        for row in range(3):
            for col in range(3):
                buttons[row][col].config(text="")
        status_label.config(text=f"Ход игрока: {current_player}")

    game_window = tk.Tk()
    game_window.title("Крестики-нолики")

    current_player = "X"
    board = [["", "", ""], ["", "", ""], ["", "", ""]]
    buttons = [[None, None, None], [None, None, None], [None, None, None]]

    status_label = tk.Label(game_window, text=f"Ход игрока: {current_player}", font=("Arial", 14))
    status_label.pack(pady=20)

    frame = tk.Frame(game_window)
    frame.pack()

    for row in range(3):
        for col in range(3):
            buttons[row][col] = tk.Button(frame, text="", font=("Arial", 20), width=5, height=2,
                                          command=lambda row=row, col=col: button_click(row, col))
            buttons[row][col].grid(row=row, column=col)

    game_window.geometry("400x450")
    game_window.mainloop()

def game_with_computer():
    def check_winner():
        for row in board:
            if row[0] == row[1] == row[2] != "":
                return row[0]
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != "":
                return board[0][col]
        if board[0][0] == board[1][1] == board[2][2] != "":
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != "":
            return board[0][2]
        return None

    def check_draw():
        for row in board:
            if "" in row:
                return False
        return True

    def minimax(is_maximizing):
        winner = check_winner()
        if winner == "O":
            return 1
        elif winner == "X":
            return -1
        elif check_draw():
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for r in range(3):
                for c in range(3):
                    if board[r][c] == "":
                        board[r][c] = "O"
                        score = minimax(False)
                        board[r][c] = ""
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for r in range(3):
                for c in range(3):
                    if board[r][c] == "":
                        board[r][c] = "X"
                        score = minimax(True)
                        board[r][c] = ""
                        best_score = min(score, best_score)
            return best_score

    def computer_move():
        best_score = -float('inf')
        move = (0, 0)
        for r in range(3):
            for c in range(3):
                if board[r][c] == "":
                    board[r][c] = "O"
                    score = minimax(False)
                    board[r][c] = ""
                    if score > best_score:
                        best_score = score
                        move = (r, c)
        board[move[0]][move[1]] = "O"
        buttons[move[0]][move[1]].config(text="O")

        if check_winner():
            messagebox.showinfo("Победа!", "Компьютер выиграл!")
            reset_game()
        elif check_draw():
            messagebox.showinfo("Ничья", "Игра закончилась вничью!")
            reset_game()
        else:
            nonlocal current_player
            current_player = "X"
            status_label.config(text=f"Ход игрока: {current_player}")

    def button_click(row, col):
        nonlocal current_player

        if board[row][col] == "":
            board[row][col] = current_player
            buttons[row][col].config(text=current_player)

            if check_winner():
                messagebox.showinfo("Победа!", f"Игрок {current_player} выиграл!")
                reset_game()
            elif check_draw():
                messagebox.showinfo("Ничья", "Игра закончилась вничью!")
                reset_game()
            else:
                current_player = "O"
                status_label.config(text=f"Ход игрока: {current_player}")
                computer_move()

    def reset_game():
        nonlocal board, current_player
        board = [["", "", ""], ["", "", ""], ["", "", ""]]
        current_player = "X"
        for row in range(3):
            for col in range(3):
                buttons[row][col].config(text="")
        status_label.config(text=f"Ход игрока: {current_player}")

    game_window = tk.Tk()
    game_window.title("Крестики-нолики")

    current_player = "X"
    board = [["", "", ""], ["", "", ""], ["", "", ""]]
    buttons = [[None, None, None], [None, None, None], [None, None, None]]

    status_label = tk.Label(game_window, text=f"Ход игрока: {current_player}", font=("Arial", 14))
    status_label.pack(pady=20)

    frame = tk.Frame(game_window)
    frame.pack()

    for row in range(3):
        for col in range(3):
            buttons[row][col] = tk.Button(frame, text="", font=("Arial", 20), width=5, height=2,
                                          command=lambda row=row, col=col: button_click(row, col))
            buttons[row][col].grid(row=row, column=col)

    game_window.geometry("400x450")
    game_window.mainloop()

window = tk.Tk()
window.title("Крестики-нолики")

label = tk.Label(window, text="Выберите режим игры", font=("Arial", 14))
label.pack(pady=20)

btn_human = tk.Button(window, text="Играть с человеком", font=("Arial", 12), command=lambda: start_game("human"))
btn_human.pack(pady=10)

btn_computer = tk.Button(window, text="Играть с компьютером", font=("Arial", 12), command=lambda: start_game("computer"))
btn_computer.pack(pady=10)

window.geometry("300x200")
window.mainloop()