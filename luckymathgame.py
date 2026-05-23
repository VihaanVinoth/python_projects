import math
import random as rnd
from math import sqrt, factorial

def lucky_math_game():
    print(f"Available math tools: {dir(math)}")
    print("-" * 30)

    rnd.seed(42)
    operations = ['+', '-', '*', 'sqrt', 'factorial']


    for i in range(6):
        num1 = rnd.randint(1, 10)
        num2 = rnd.randint(1, 10)
        operations = rnd.choice(operations)
        if operations == 'sqrt':
            answer = math.sqrt(num1)
            print(f"Question {i}: sqrt({num1}) = {answer:.2f}")
        elif operations == 'factorial':
            answer = math.factorial(num1)
            print(f"Question {i}: factorial({num1}) = {answer}")
        else:
            if operations == '+': 
                answer = num1 + num2
            elif operations == '-': 
                answer = num1 - num2
            elif operations == '*': 
                answer = num1 * num2
            print(f"Question {i}: {num1} {operations} {num2} = {answer}")
    
    test_val = 4.233674
    print(f"\nRounding demo for {test_val}:")
    print(f"  ceil:  {math.ceil(test_val)}")   
    print(f"  floor: {math.floor(test_val)}")
    print(f"  trunc: {math.trunc(test_val)}") 
    print(f"  round: {round(test_val)}") 

    side_a, side_b = 6, 9
    hypotenuse = math.hypot(side_a, side_b)
    print(f"\nHypotenuse of sides {side_a} and {side_b} is {hypotenuse:.2f}")

    print("Complete")

lucky_math_game()