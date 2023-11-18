from django.shortcuts import render

# Create your views here.
import random
import time


def start():
    marks = []
    num_marks = random.choice([4, 5])
    for mark in range(num_marks):
        gen_mark = random.randrange(0, 100)
        if gen_mark in marks:
            mark -= 1
            continue
        marks.append(gen_mark)
    print(marks)

    for turns in range(100):
        mark = random.choice(marks)
        time.sleep(3)
        print(mark)
