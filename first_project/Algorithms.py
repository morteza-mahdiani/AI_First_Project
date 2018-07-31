

class Algorithms:
    def BFS(self, problem):
        sequenceOfactions = []
        listOfVisitedNodes = []
        queue = []

        node = Node(None, None, problem.getInitialState(), 0)
        queue.append(node)

        while len(queue) > 0:
            node = queue.pop(0)
            listOfVisitedNodes.append(node)
            sequenceOfactions = problem.getAction(node.state)
            for e in sequenceOfactions:
                newNode = Node(node, e, problem.result(node.state, e), 0)
                if problem.goalTest(newNode.state):
                    return self.getSolution(newNode)
                if newNode not in listOfVisitedNodes\
                        and newNode not in queue:
                    queue.append(newNode)

        return None

    def DFS(self, problem):
        sequenceOfactions = []
        listOfVisitedNodes = []
        queue = []

        node = Node(None, None, problem.getInitialState(), 0)
        queue.append(node)

        while len(queue) > 0:
            node = queue.pop()
            listOfVisitedNodes.append(node)
            sequenceOfactions = problem.getAction(node.state)
            for e in sequenceOfactions:
                newNode = Node(node, e, problem.result(node.state, e), 0)
                if problem.goalTest(newNode.state):
                    return self.getSolution(newNode)
                if newNode not in listOfVisitedNodes\
                        and newNode not in queue:
                    queue.append(newNode)

        return None

    def DLimitedS(self, problem, limitedDepth):
        sequenceOfactions = []
        listOfVisitedNodes = []
        queue = []
        depth = 0

        node = Node(None, None, problem.getInitialState(), 0)
        queue.append(node)

        while len(queue) > 0 and depth < limitedDepth:
            node = queue.pop()
            listOfVisitedNodes.append(node)
            sequenceOfactions = problem.getAction(node.state)
            for e in sequenceOfactions:
                newNode = Node(node, e, problem.result(node.state, e), 0)
                if problem.goalTest(newNode.state):
                    return self.getSolution(newNode)
                if newNode not in listOfVisitedNodes\
                        and newNode not in queue:
                    queue.append(newNode)
            depth += 1

        return None

    def IterativeDFS(self, problem):
        sequenceOfactions = []
        listOfVisitedNodes = []
        queue = []
        for limitedDepth in range(2, 100, 3):
            depth = 0

            node = Node(None, None, problem.getInitialState(), 0)
            queue.append(node)

            while len(queue) > 0 and depth < limitedDepth:
                node = queue.pop()
                listOfVisitedNodes.append(node)
                sequenceOfactions = problem.getAction(node.state)
                for e in sequenceOfactions:
                    newNode = Node(node, e, problem.result(node.state, e), 0)
                    if problem.goalTest(newNode.state):
                        return self.getSolution(newNode)
                    if newNode not in listOfVisitedNodes\
                            and newNode not in queue:
                        queue.append(newNode)
                depth += 1

        return None

    def UniformCost(self, problem):
        sequenceOfactions = []
        listOfVisitedNodes = []
        queue = []

        node = Node(None, None, problem.getInitialState(), 0)
        queue.append(node)

        while len(queue) > 0:
            queue = list(self.sortListOfNodes(queue))
            node = queue.pop()
            listOfVisitedNodes.append(node)
            sequenceOfactions = problem.getAction(node.state)
            for e in sequenceOfactions:
                newNode = Node(node, e, problem.result(node.state, e), problem.getCost(None, None, None) + node.cost)
                if problem.goalTest(newNode.state):
                    return self.getSolution(newNode)
                if newNode not in listOfVisitedNodes\
                        and newNode not in queue:
                    queue.append(newNode)

        return None

    def AStar(self, problem):
        sequenceOfactions = []
        listOfVisitedNodes = []
        queue = []

        node = Node(None, None, problem.getInitialState(), 0)
        queue.append(node)

        while len(queue) > 0:
            queue = list(self.sortListOfNodes(queue))
            node = queue.pop()
            listOfVisitedNodes.append(node)
            sequenceOfactions = problem.getAction(node.state)
            for e in sequenceOfactions:
                newNode = Node(node, e, problem.result(node.state, e),problem.getCost(None, None, None)\
                               + node.cost + problem.heuristic(problem.result(node.state, e)))
                if problem.goalTest(newNode.state):
                    return self.getSolution(newNode)
                if newNode not in listOfVisitedNodes\
                        and newNode not in queue:
                    queue.append(newNode)

        return None

    def BiDirectional(self, problem, GoalNode):
        sequenceOfactions1 = []
        listOfVisitedNodes1 = []
        queue1 = []

        sequenceOfactions2 = []
        listOfVisitedNodes2 = []
        queue2 = []

        node1 = Node(None, None, problem.getInitialState(), 0)
        queue1.append(node1)

        node2 = GoalNode
        queue2.append(node2)

        while len(queue1) > 0:
            node2 = queue2.pop(0)
            listOfVisitedNodes2.append(node2)
            sequenceOfactions2 = problem.getAction(node2.state)
            for e in sequenceOfactions2:
                newNode2 = Node(node2, e, problem.result(node2.state, e), 0)
                if problem.goalTest(newNode2.state):
                    return self.getSolution(newNode2)
                if newNode2 not in listOfVisitedNodes2\
                        and newNode2 not in queue2:
                    queue2.append(newNode2)

            node1 = queue1.pop(0)
            listOfVisitedNodes1.append(node1)
            sequenceOfactions1 = problem.getAction(node1.state)
            for e in sequenceOfactions1:
                newNode1 = Node(node1, e, problem.result(node1.state, e), 0)
                if self.checkExist(newNode1, queue2):
                    tempList = self.getSolution(newNode1.reverse()) + \
                    self.getSolution(queue2[self.checkIndex(newNode1, queue2)])
                    return tempList
                if newNode1 not in listOfVisitedNodes1\
                        and newNode1 not in queue1:
                    queue1.append(newNode1)
        return None

    def checkExist(self, list1, node):
        for e in list1:
            if e == node:
                return True

    def checkIndex(self, list1, node):
        for i in range(0, len(list1)):
            if list1[i]== node:
                return i

    def sortListOfNodes(self, ListOfNodes):
        return sorted(ListOfNodes, key= lambda Node: Node.cost)

    def getSolution(self, finalNode):
        solution = []
        currNode = finalNode
        while currNode != None:
            solution.append(currNode.action)
            currNode = currNode.parent
        return solution

class Node:
    def __init__(self, parent, action, state, cost):
        self.parent = parent
        self.action = action
        self.state = state
        self.cost = cost

    def __eq__(self, other):
        return self.state == other.state



