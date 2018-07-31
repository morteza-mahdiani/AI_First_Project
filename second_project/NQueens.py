from random import randrange

class NQueens:

    def getInitialState(self):
        state = State([0, 1, 2, 3, 4, 5, 6, 7]).copy()
        return state

    def getStocasticInitialState(self, ):
        nextState = State([0, 1, 2, 3, 4, 5, 6, 7]).copy()
        for i in range(0, 20):
            i = randrange(0, 8)
            j = randrange(0, 8)
            temp = nextState.position[i]
            nextState.position[i] = nextState.position[j]
            nextState.position[j] = temp
        return nextState

    def getAction(self, state):
        sequenceOfAction = []
        for i in range(0, 8):
            for j in range(i + 1, 8):
                action = Action(i, j)
                sequenceOfAction.append(action)
        return sequenceOfAction


    def result(self, state, action):
        nextState = state.copy()
        actionOnState = action

        temp = nextState.position[actionOnState.firstPosition]
        nextState.position[actionOnState.firstPosition] = \
            nextState.position[actionOnState.secondPosition]
        nextState.position[actionOnState.secondPosition] = temp

        return nextState


    def fitness(self, state):
        number = 0
        for i in range(0, 8):
            for j in range(i+1  , 8):
                if (j - i == abs(state.position[j] - state.position[i])):
                    number += 1

        return -1 * number

    # def goelTest(self, state):
    #     return None

    # def getCost(self, paretState, childState, action):
    #     return  0

class State:
        def __init__(self, position):
            self.position = position

        def copy(self):
            return State(list(self.position))

class Action:
        def __init__(self, firstPosition, secondPosition):
            self.firstPosition = firstPosition
            self.secondPosition = secondPosition

        def __str__(self):
            return self.firstPosition + ", " + self.secondPosition

