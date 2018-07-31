import math
from numpy import random


class Equation:

    def initialPopuation(self):
        individual = random.uniform(0.2, 3.14)
        return individual

    def crossOver(self, father, mother):
        return (father + mother)/2


    def mutate(self, inputVal):
        mean = 0
        standardDeviation = 0.01
        while True:
            test = random.normal(mean, standardDeviation)
            test += inputVal
            if test > 0.2 and test < 3.14 :
                return test

    def fitnessGA(self, inputVal):
        rightVal = math.sin( inputVal)
        leftVal = math.pow(inputVal, 2) - inputVal

        return   - abs(rightVal- leftVal)

    def goalTest(self, inputVal):
        if abs(math.sin( inputVal) - math.pow(inputVal, 2) + inputVal) < 0.001:
            return True
        return False


