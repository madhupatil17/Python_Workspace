class QuizzBrain:
    def __init__(self, question_bank):
        self.question_number = 1
        self.question_bank = question_bank
        self.score = 0

    def next_question(self):
        for _ in range(len(self.question_bank)):
            print(f"Q {self.question_number}: {self.question_bank[self.question_number-1].text} (True/False)")
            guess = input("Your answer? ")
            if guess == self.question_bank[self.question_number-1].answer:
                print("Correct!")
                self.score += 1
                print(f"Your score is {self.score}/{len(self.question_bank)}", end='\n\n')
            else:
                print(f"Your answer is wrong. Correct answer is {self.question_bank[self.question_number-1].answer}")
                print(f"Your score is {self.score}/{len(self.question_bank)}", end='\n\n')
            self.question_number += 1

