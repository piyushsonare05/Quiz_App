import time

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# Define your list of questions
questions = [
    Question("Who invented the Python programming language?\n(a) Guido van Rossum\n(b) Dennis Ritchie\n(c) James Gosling\n", "a"),
    Question("What is the capital city of Madhya Pradesh?\n(a) Bhopal\n(b) Indore\n(c) Jabalpur\n", "a"),
    Question("What is the name of the first supercomputer?\n(a) ENIAC\n(b) CRAY-1\n(c) Colossus\n", "a"),
    Question("What is the size of 1 GB in KB?\n(a) 1024 KB\n(b) 1000 KB\n(c) 1048576 KB\n", "c"),
    Question("Who invented the computer?\n(a) Alan Turing\n(b) Charles Babbage\n(c) Tim Berners-Lee\n", "b")
]

def run_quiz(questions):
    score = 0
    start_time = time.time()
    for question in questions:
        answer = input(question.prompt).lower()
        if answer == question.answer:
            score += 1
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Time taken:", round(elapsed_time, 2), "seconds")
    print("You got", score, "out of", len(questions), "correct!")
    return elapsed_time, score

def update_leaderboard(player_name, score, time_taken):
    leaderboard.append((player_name, score, time_taken))
    leaderboard.sort(key=lambda x: (x[1], -x[2]), reverse=True)  # Sort by score then by time taken

def display_leaderboard():
    print("Leaderboard:")
    for i, (name, score, time_taken) in enumerate(leaderboard, start=1):
        print(f"{i}. {name}: Score - {score}")

leaderboard = []

if __name__ == "__main__":
    player_name = input("Enter your name: ")
    elapsed_time, score = run_quiz(questions)
    update_leaderboard(player_name, score, elapsed_time)
    display_leaderboard()
    print("--Dhanyawad--")
