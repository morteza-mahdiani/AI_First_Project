import math

from Problem import problem


class NQueens(problem):
    def getInitialState(self):
        position = [1, 2, 3, 4, 5]
        state = State(position)
        return state

    def getAction(self, state):
        sequenceOfNextAction = []
        for i in range(0, len(state.position)):
            for j in range(i+1, len(state.position)):
                action = Action(i, j)
                sequenceOfNextAction.append(action)
        return sequenceOfNextAction

    def result(self, state, action):
        position = list(state.position)

        temp = position[action.secondPosition]
        position[action.secondPosition] = position[action.firstPosition]
        position[action.firstPosition] = temp

        newState = State(position)
        return newState

    def goalTest(self, state):
        for i in range(0, len(state.position)):
            for j in range(i+1, len(state.position)):
                if math.fabs(i - j) == math.fabs(state.position[i] - state.position[j]):
                    return False
        return True

    def heuristic(self, state):
        rValue = 0
        for i in range(0, len(state.position)):
            for j in range(i+1, len(state.position)):
                if math.fabs(i - j) == math.fabs(state.position[i] - state.position[j]):
                    rValue +=1
        return rValue / 2

    def getCost(self, parentState, action, state):
        return 1

class State():
    def __init__(self, position):
        self.position = list(position)

    def __eq__(self, other):
        for i in range(0, len(self.position)):
            if self.position[i] != other.position[i]:
                return False
        return True

class Action():
    def __init__(self, firstPosition, secondPosition):
        self.firstPosition = firstPosition
        self.secondPosition = secondPosition