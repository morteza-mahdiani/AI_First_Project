import Algorithms
from Equation import Equation
from NQueens import NQueens

nq = NQueens()
eq = Equation()

# print Algorithms.hillClimbing(nq)
# print str('******************************************************')
# print Algorithms.stocasticHillClimbing(nq)
# print str('******************************************************')
# print Algorithms.randomRestartHillClimbing(nq)
# print str('******************************************************')
# print Algorithms.firstChoiceHillClimbing(nq)
# print str('******************************************************')
# print Algorithms.SimulatedAnnealing(nq)
# print str('******************************************************')
print Algorithms.GA(eq)
print str('******************************************************')