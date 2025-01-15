import tkinter as tk
from tkinter import messagebox
import random

# List of questions (example format with lyrics)
questions = [
    {"question": "Wish we could turn back time, to the ___ days", "answer": "good old"},
    {"question": "I wake up fine and dandy, but then by the time I find it ___", "answer": "handy"},
    {"question": "Sometimes a certain smell will take me back to when I was ___", "answer": "young"},
    # Add more questions here
]

# Background images for each question (example paths)
backgrounds = [
    "images/twenty_one_pilots_1.jpg",
    "images/twenty_one_pilots_2.jpg",
    "images/twenty_one_pilots_3.jpg",
    # Add more image paths here
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("twenty one pilots Quiz")
        self.root.geometry("800x600")

        self.score = 0
        self.current_question = 0
        
        # Frame for the question and input
        self.quiz_frame = tk.Frame(self.root, bg="white")
        self.quiz_frame.pack(fill=tk.BOTH, expand=True)

        # Canvas for background image
        self.canvas = tk.Canvas(self.quiz_frame, width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Question label
        self.question_label = tk.Label(self.quiz_frame, text="", font=("Arial", 20), wraplength=600, bg="white")
        self.question_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        # Answer entry
        self.answer_entry = tk.Entry(self.quiz_frame, font=("Arial", 16))
        self.answer_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Submit button
        self.submit_button = tk.Button(self.quiz_frame, text="Submit", font=("Arial", 14), command=self.check_answer)
        self.submit_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        self.load_question()

    def load_question(self):
        if self.current_question < len(questions):
            question = questions[self.current_question]
            background = backgrounds[self.current_question % len(backgrounds)]

            # Update question text
            self.question_label.config(text=question["question"])

            # Update background image
            self.bg_image = tk.PhotoImage(file=background)  # Use PhotoImage for background
            self.canvas.create_image(0, 0, image=self.bg_image, anchor=tk.NW)
        else:
            self.end_quiz()

    def check_answer(self):
        user_answer = self.answer_entry.get().strip().lower()
        correct_answer = questions[self.current_question]["answer"].lower()

        if user_answer == correct_answer:
            self.score += 1

        self.current_question += 1
        self.answer_entry.delete(0, tk.END)
        self.load_question()

    def end_quiz(self):
        messagebox.showinfo("Quiz Finished", f"Your score is {self.score}/{len(questions)}!")
        self.root.quit()

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
