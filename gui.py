import tkinter as tk
import csv

class VoteGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.candidates = {
            "Candidate 1": 0,
            "Candidate 2": 0,
            "Candidate 3": 0
        }

    def create_widgets(self):
        self.vote_label = tk.Label(self, text="Vote Menu:")
        self.vote_label.pack()

        self.name_label = tk.Label(self, text="Enter Your Name:")
        self.name_label.pack()

        self.name_input = tk.Entry(self)
        self.name_input.pack()

        self.result_label = tk.Label(self)
        self.result_label.pack()

        self.candidate_label = tk.Label(self, text="Candidate Menu:")
        self.candidate_label.pack()

        self.selected_candidate = tk.StringVar()
        self.candidate_buttons = []
        for candidate in range(1, 4):
            button = tk.Radiobutton(
                self,
                text=f"Candidate {candidate}",
                variable=self.selected_candidate,
                value=str(candidate),
                state=tk.DISABLED
            )
            button.pack()
            self.candidate_buttons.append(button)

        self.exit_button = tk.Button(self, text="Vote", command=self.vote)
        self.exit_button.pack()

        self.name_input.bind("<KeyRelease>", self.enable_candidate_buttons)

    def enable_candidate_buttons(self, event):
        name = self.name_input.get()
        if name:
            for button in self.candidate_buttons:
                button.config(state=tk.NORMAL)
        else:
            for button in self.candidate_buttons:
                button.config(state=tk.DISABLED)

        #try and accept error handling to accept only letters. No spaces, numbers, or special characters.
        try:
           if name.isalpha():
               for button in self.candidate_buttons:
                   button.config(state=tk.NORMAL)
           else:
               for button in self.candidate_buttons:
                   button.config(state=tk.DISABLED)
        except:
           for button in self.candidate_buttons:
               button.config(state=tk.DISABLED)



    def save_vote(self, name, response):
        with open("votes.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, response])

    def vote(self):
        name = self.name_input.get()
        response = self.selected_candidate.get()

        if name and response:
            self.save_vote(name, response)

            self.name_input.delete(0, tk.END)
            self.selected_candidate.set("")
            self.enable_candidate_buttons(None)

            self.result_label.config(text=f"Thank you for voting, {name}! You voted for Candidate {response}.")

            if response in ["1", "2", "3"]:
                candidate = f"Candidate {response}"
                self.candidates[candidate] += 1

                print("Vote Count:")
                for candidate, count in self.candidates.items():
                    print(f"{candidate}: {count}")
        else:
            self.result_label.config(text="Please enter your name and select a candidate.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Voting System")

    vote_gui = VoteGUI(root)
    vote_gui.pack()

    root.mainloop()