import tkinter as tk
from gui import VoteGUI

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Voting System")
    root.geometry("250x250")
    root.resizable(False, False)
    root.config(bg="red")

    vote_gui = VoteGUI(root)
    vote_gui.pack()

    root.mainloop()  