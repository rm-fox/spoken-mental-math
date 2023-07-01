
# Script out first then optimise program
import pytest
import random
from gtts import gTTS
import os
import sys

# Shell will loop through logic (X times) that looks like
# 1. Algo that creates math question of random type
#    Maths question taken from class with several methods
#    First will be addition (<100) and multiplication <(12)
# 2. Question then spoken through speaker
# 3. Requires user response through cli
# 4. Finish shell loop and report score

class Question:
    def addition(self):
        a = random.randrange(0, 100, 1)
        b = random.randrange(0, 100, 1)
        q = "What is {} plus {}?".format(a, b)
        self.read_question(q)
        return a + b, q
    
    def multiplication(self):
        a = random.randrange(0, 100, 1)
        b = random.randrange(0, 10, 1)
        q = "What is {} times {}?".format(a, b)
        self.read_question(q)
        return a * b, q
    
    def mulitplication_2dig(self):
        a = random.randrange(0, 100, 1)
        b = random.randrange(0, 100, 1)
        q = "What is {} times {}?".format(a, b)
        self.read_question(q)
        return a * b, q
    
    def addition_decimal(self):
        a = round(random.uniform(0, 100), 2)
        b = round(random.uniform(0, 100), 2)
        q = "What is {} plus {}?".format(a, b)
        self.read_question(q)
        return a + b, q
    
    def division(self):
        a = random.randrange(0, 100, 1)
        b = random.randrange(0, 10, 1)
        divisor_val = a*b
        q = "What is {} divided by {}?".format(divisor_val, b)
        self.read_question(q)
        return a, q

    def read_question(self, q):
        myobj = gTTS(text=q, lang='en', slow=False)
        myobj.save("welcome.mp3")
        os.system("afplay welcome.mp3")

class Test:
    def __init__(self, length):
        self.score = 0
        self.length = length

    def loop_test(self):
        for _ in range(self.length):
            q = Question()

            operations = {
                1: q.addition,
                2: q.multiplication,
                3: q.addition_decimal,
                4: q.mulitplication_2dig,
                5: q.division
            }
            rand = random.randint(1, 5)
            operation = operations.get(rand)
            if operation:
                ans, c = operation()

            user_answer = input()
            if str(user_answer) == str(ans):
                self.score += 1 
            else:
                print("^ Wrong - {}".format(c))

        print("You scored {}/{}".format(self.score, self.length))

run = Test(int(sys.argv[1])) # set when developing
run.loop_test()




