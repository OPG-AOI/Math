import random

score = 0
operators = {
  "+": lambda x, y: x + y,
  "-": lambda x, y: x - y,
  "*": lambda x, y: x * y,
  "/": lambda x, y: x / y
}


def generate_question(difficulty):
  if difficulty == "easy":
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
  elif difficulty == "medium":
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
  else:
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
  operator = random.choice(list(operators.keys()))
  question = f"What is {num1} {operator} {num2}?"
  answer = operators[operator](num1, num2)
  return question, answer


difficulty = input("Select difficulty level (easy, medium, hard): ")
play_again = ""
while play_again != "q":
  question, answer = generate_question(difficulty)
  user_answer = input(question)
  if user_answer == str(answer):
    print("Your Right!")
    score += 1
  else:
    print("Try again!")
  play_again = input("Press 'q' to quit")

print("Your final score is: ", score)
