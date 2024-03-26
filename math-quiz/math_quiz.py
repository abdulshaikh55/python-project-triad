import random
import time

OPERATORS = ["+", "-", "*"]
MAX_OPERAND = 12
MIN_OPERAND = 3
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0
input("Press enter to start!")
print("----------------------")
start_time = time.time()
i = 1
while i <= TOTAL_PROBLEMS:
    expr, ans = generate_problem()
    while True:
        guess = input("Problem #" + str(i) + " : " + expr + " = ")
        if guess == str(ans):
            break
        wrong += 1
    i += 1
        
end_time = time.time()

total_time = round (end_time - start_time, 2)

print("Yay! You finished in", total_time)