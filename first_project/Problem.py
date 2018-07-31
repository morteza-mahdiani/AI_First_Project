
class problem:
    def getInitialState(self):
        return None

    def getAction(self, state):
        return None

    def result(self, state, action):
        return list

    def goalTest(self, state):
        return bool

    def getCost(self, parentState, action, state):
        return int
