

from Problem import problem


class RobotRouting(problem):
    constraints = [[1, 2, 1, 3], [2, 2, 2, 3], [2, 2, 3, 2],
            [0, 4, 0, 5], [1, 4, 1, 5], [2, 4, 2, 5],
            [3, 4, 3, 5], [4, 4, 4, 5], [4, 0, 5, 0], [4, 1, 5, 1],
            [4, 2, 5, 2], [4, 3, 5, 3], [4, 4, 5, 4]]
    def getInitialState(self):
        state = State(1 ,1)
        return state

    def getAction(self, state):
        sequenceOfActions = []

        action = Action(1, 0)
        sequenceOfActions.append(action)
        action = Action(0, 1)
        sequenceOfActions.append(action)

        return sequenceOfActions

    def result(self, state, action):
        nextState = State(state.i + action.right, state.j + action.down)
        set = True
        for i in range(0, len(RobotRouting.constraints)):
            if RobotRouting.constraints[i][0] == state.i \
                and RobotRouting.constraints[i][1] == state.j \
                and RobotRouting.constraints[i][2] == nextState.i \
                and RobotRouting.constraints[i][3] == nextState.j:
                set =False
        if set == True:
            return nextState
        else:
            return state

    def goalTest(self, state):
        if state.i == 4 and state.j == 4:
            return True
        else:
            return False

    def heuristic(self, state):
        rValue = (4-state.i) + (4-state.j)
        return rValue / 2

    def getCost(self, parentState, action, state):
        return 1

class State:
    def __init__(self, i, j):
        self.i = i
        self.j = j
class Action:
    def __init__(self, right , down):
        self.right = right
        self.down = down

