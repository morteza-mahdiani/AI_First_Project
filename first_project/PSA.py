from Algorithms import Node
from NQueens import State


class PSA:
    def solving(self, problem, algorithm):
        print algorithm.BFS(problem)
        # print algorithm.DFS(problem)
        # print algorithm.IterativeDFS(problem)
        # print algorithm.UniformCost(problem)
        # print algorithm.AStar(problem)
        #
        # print algorithm.DLimitedS(problem, 20)

        # position = [5, 3, 1, 4, 2]
        # state = State(position)
        # node = Node(None,None, state, 0)
        # print algorithm.BiDirectional(problem, node)
