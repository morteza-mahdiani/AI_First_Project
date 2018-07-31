from Algorithms import Algorithms
from NQueens import NQueens
from PSA import PSA
from RobotRouting import RobotRouting


class Main:
    nquenns = NQueens()
    robotrouting = RobotRouting()

    algorithms = Algorithms()
    psa = PSA()

    psa.solving(nquenns, algorithms)

