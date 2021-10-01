import random

def ASD(score=random.uniform(-999, 999)):
    if score < 0:
        print("Invalid score")
    else:
        if score > 100:
            print("Invalid score")
        if 50 <= score < 90:
            print("Passable")
        if 90 <= score <= 100:
            print("Excellent")
    if 0 < score < 50:
        print("Bad")
ASD()