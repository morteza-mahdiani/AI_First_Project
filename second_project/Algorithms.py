from numpy import random
import matplotlib.pyplot as plt
import numpy as np
from random import randrange
import math


#######hill#climbing#
from numpy.core.fromnumeric import size


def hillClimbing(problem):
    steps = 0
    expanded = 0
    visited = 0
    fitnessMean = 0
    currentState = problem.getInitialState()
    fitnessMean += problem.fitness(currentState)
    expanded += 1
    while (True):
        steps += 1
        listOfNeighbors = problem.getAction(currentState)
        bestval = problem.fitness(currentState)
        bestState = None
        for action in listOfNeighbors:
            visited += 1
            new = problem.result(currentState, action)
            if bestval < problem.fitness(new):
                bestState = new
                bestval = problem.fitness(new)
        if bestState is None:
            print "steps: " + str(steps)
            print "visited nodes: " + str(visited)
            print "expanded nodes: " + str(expanded)
            print "general fitness: " + str(fitnessMean / expanded)
            return  currentState
        currentState = bestState
        fitnessMean += problem.fitness(currentState)
        expanded += 1


########stocastic#hill#climbing#


def stocasticHillClimbing(problem):
    steps = 0
    expanded = 0
    visited = 0
    fitnessMean = 0
    currentState = problem.getInitialState()
    fitnessMean += problem.fitness(currentState)
    expanded += 1
    listOfBest = []
    while (True):
        steps += 1
        listOfNeighbors = problem.getAction(currentState)
        bestval = problem.fitness(currentState)
        bestState = None
        for action in listOfNeighbors:
            visited += 1
            new = problem.result(currentState, action)
            if bestval < problem.fitness(new):
                bestState = new
                bestval = problem.fitness(new)
        for action in listOfNeighbors:
            if problem.fitness(problem.result(currentState, action)) == bestval:
                listOfBest.append(problem.result(currentState, action))
        if bestState is None:
            print "steps: " + str(steps)
            print "visited nodes: " + str(visited)
            print "expanded nodes: " + str(expanded)
            print "general fitness: " + str(fitnessMean / expanded)
            return  currentState
        currentState = listOfBest[randrange(len(listOfBest))]
        fitnessMean += problem.fitness(currentState)
        expanded += 1


########Random#Restart#Hill#Climbing#


def  randomRestartHillClimbing(problem):
    count = 0
    steps = 0
    expanded = 0
    visited = 0
    fitnessMean = 0
    currentState = problem.getInitialState()
    fitnessMean += problem.fitness(currentState)
    expanded += 1
    listOfBest = []
    while (True):
        steps += 1
        listOfNeighbors = problem.getAction(currentState)
        bestval = problem.fitness(currentState)
        bestState = None
        for action in listOfNeighbors:
            visited += 1
            new = problem.result(currentState, action)
            if bestval < problem.fitness(new):
                bestState = new
                bestval = problem.fitness(new)
        if bestState is None:
            listOfBest.append(currentState)
            count += 1
            if count == 10:
                bestTemp = currentState
                for state in listOfBest:
                    if problem.fitness(state) >= problem.fitness(bestTemp):
                        bestTemp = state
                print "steps: " + str(steps)
                print "visited nodes: " + str(visited)
                print "expanded nodes: " + str(expanded)
                print "general fitness: " + str(fitnessMean / expanded)
                return bestTemp
            currentState = problem.getStocasticInitialState()
            fitnessMean += problem.fitness(currentState)
            expanded += 1
        else:
            currentState = bestState
            fitnessMean += problem.fitness(currentState)
            expanded += 1


########first#Choice#Hill#Climbing#


def firstChoiceHillClimbing(problem):
    steps = 0
    expanded = 0
    visited = 0
    fitnessMean = 0
    currentState = problem.getInitialState()
    fitnessMean += problem.fitness(currentState)
    expanded += 1
    while (True):
        steps += 1
        listOfNeighbors = problem.getAction(currentState)
        bestval = problem.fitness(currentState)
        bestState = None
        action = listOfNeighbors[randrange(len(listOfNeighbors))]
        new = problem.result(currentState, action)
        visited += 1
        if bestval < problem.fitness(new):
            bestState = new
            bestval = problem.fitness(new)
        if bestval == problem.fitness(currentState):
            print "steps: " + str(steps)
            print "visited nodes: " + str(visited)
            print "expanded nodes: " + str(expanded)
            print "general fitness: " + str(fitnessMean / expanded)
            return  currentState
        if bestState is not None :
            currentState = bestState
            fitnessMean += problem.fitness(currentState)
            expanded += 1


########Simulated#Annealing#


def SimulatedAnnealing(problem):
    currentState = problem.getInitialState()
    steps = 0
    expanded = 0
    visited = 0
    fitnessMean = 0
    test = []
    t = 0
    while True:
        steps += 1
        tempereture = schedule(t, 1)
        if tempereture == 0.:
            print "steps: " + str(steps)
            print "visited nodes: " + str(visited)
            print "expanded nodes: " + str(expanded)
            print "general fitness: " + str(fitnessMean / expanded)
            # print size(test)
            # plt.plot(test)
            # plt.xlabel('number of iteration')
            # plt.ylabel('fitness')
            # plt.title('equation = 313 - t')
            # plt.show()
            return currentState
        listOfActions = problem.getAction(currentState)
        next = problem.result(currentState,
                              listOfActions[randrange(len( listOfActions))])
        visited += 1

        deltaE = problem.fitness(next) - problem.fitness(currentState)
        test.append( problem.fitness(currentState))
        if deltaE > 0 :
            currentState = next
            expanded += 1
            fitnessMean += problem.fitness(currentState)
        else:
            if (np.random.uniform(0, 1) <= \
                           probability(problem.fitness(next) , problem.fitness(currentState), tempereture)):
                currentState = next
                expanded += 1
                fitnessMean += problem.fitness(currentState)
        t += 1

def schedule( t, type):
    if type == 1:
        return 313 - t
    if type == 2:
        return math.log(313 - t, 2)
    if type == 3:
        return 1024 - math.pow(t, 2)


def probability( oldCost, newCost, temprature):
    return math.exp((oldCost - newCost)/ temprature)


########GA#


def randomSelection(population, problemGA):
    population.sort(key =lambda x: problemGA.fitnessGA(x))
    p = 0.6
    for i in range(0, len(population)):
        if random.uniform(0, 1) < p:
            return population[len(population) - 1 - i]
    return population[len(population) - 1]

def mean(population, problemGA):
    population.sort(key =lambda x: problemGA.fitnessGA(x))
    agg = 0
    for i in range(0, len(population)):
        agg += population[i]
    return  agg / len(population)

def good(population, problemGA):
    population.sort(key =lambda x: problemGA.fitnessGA(x))
    return population[0]

def bad(population, problemGA):
    population.sort(key =lambda x: problemGA.fitnessGA(x))
    return population[len(population) - 1]

def GA(problemGA):
    steps = 0
    population = []
    bestVals = []
    badVals = []
    meanVals = []
    for i in range(0, 20):
        test = problemGA.initialPopuation()
        population.append(test)
    while True:
        steps += 1
        newPopulation = []
        for i in range(0, len(population)):
            x = randomSelection(population, problemGA)
            y = randomSelection(population, problemGA)
            child = problemGA.crossOver(x, y)
            if random.random() < 0.2:
                child = problemGA.mutate(child)
            newPopulation.append(child)
        population = newPopulation

        bestVals.append(good(population, problemGA))
        badVals.append(bad(population, problemGA))
        meanVals.append(mean(population, problemGA))

        population.sort(key=lambda x: problemGA.fitnessGA(x))
        best = population[len(population) - 1]
        if problemGA.goalTest(best):
            plt.plot(meanVals)
            plt.xlabel('number of iteration')
            plt.ylabel('fitness')
            plt.title('GA_meanVals')
            plt.show()
            # print "steps: " + str(steps) + "  population: " + str(size(population)) + "  answer: "
            return best



