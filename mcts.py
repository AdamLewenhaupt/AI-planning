import mcts.mcts as mcts

from traveller import Traveller
from map import Map
from sys import argv
import time

C = 50
TOTAL_ITERATIONS = 2000
SHOWN = {}

def statistics(cond, data, x):
    """
    Calculate the percentage of simulations 
    that ran by a specific state.

    :param cond: The visits to the parent node
    :param data: The statistics to base the calculation upon
    :param x: The state to evaluate for.
    """
    h = hash(x)

    if h in data.keys():
        if not h in SHOWN.keys():
            print("%.2f%%, %.2f%%, %s" % (data[h] / cond[0] * 100, data[h] / TOTAL_ITERATIONS * 100, str(x)))
        SHOWN[h] = True
        cond[0] = data[h]

def report(mc):
    """
    Print the statistics for
    all solutions.

    :param mc: A MCTS instance
    """

    used = {}

    print("Report:")
    solutions = []
    mc.findSolutions(mc.initialState, solutions)

    for s in solutions:
        # Hack to get a reference
        N = [TOTAL_ITERATIONS]
        t = s.traveller
        t.rewalk(lambda x: statistics(N, mc.counter, x))

class TravelAgent(mcts.Agent):
    """ Provides an interface between the Traveller and the MCTS
    """

    def __init__(self, traveller, worstStraightPath):
        self.traveller = traveller
        self.worstStraightPath = worstStraightPath

    def findLegalNextStates(self):
        moves = self.traveller.findLegalMoves()
        travellers = [self.traveller.moveTo(move) for move in moves]
        return [TravelAgent(t, self.worstStraightPath) for t in travellers if t.timeElapsed < self.worstStraightPath]
        
    def score(self):
        """
        We define the score as such: 1 - elapsed-time / worst-naive-time
        This gives a function that gives minus to times > worst-naive-time
        0 to equal times
        and + to better times
        """

        if not self.isDone():
            return 0

        if self.traveller.timeElapsed < self.worstStraightPath:
            return 1

        return 0

    def isDone(self):
        return self.traveller.isAtGoal()

    def __str__(self):
        return str(self.traveller)

    def __hash__(self):
        return hash(self.traveller)
 

def byMean(agent):
    mean, var = agent.traveller.simulate(1000)
    return mean, var

def simple(agent):
    return agent.traveller.timeElapsed

def findOptimalSolution(solutions):
    """ Used to find the best option amongst the ones suggested by the MCTS.
    :param soltuions: The MCTS suggested solutions.
    """

    return min(solutions, key = simple)


def main():
    """
    python3 mcts.py (path|other)
    Run to get the best paths
    or statistics for all paths.
    """


    nameTable = {}
    with open("./data/test/register.json", encoding="UTF-8") as f:
        nameTable = eval(f.read())

    m = Map("./data/test/walk.mat", "./data/test/subway.mat", "./data/test/bus.mat")

    trips = [
            ("Tekniska högskolan", "Slussen"),
            ("Norrtull", "Slussen"),
            ("Tekniska högskolan", "Norrtull"),
            ("Tekniska högskolan", "Mariatorget"),
            ("S:t Eriksplan", "Kungsträdgården"),
            ("S:t Eriksplan", "Mariatorget"),
            ("Kungsholmen", "Zinkensdamm"),
            ("Eriksbergsgatan", "Slussen"),
            ("Eriksbergsgatan", "Odengatan"),
            ("Eriksbergsgatan", "Kungsholmen")
            ]

    for start, goal in trips:
        print("%s & %s &" % (start, goal), end=" ")
        t = Traveller(m, nameTable[start])
        t.setTarget(nameTable[goal])

        before = time.time()
        evaluate(t)
        delta = time.time() - before
        print("& %.2f \\\\ \\hline" % delta)

def evaluate(t):
    """ Evaluate a trip with MCTS
    :param t: A traveller
    """

    worstStraightPath = 999999

    for (target, kind, time) in t.findLegalMoves():
        if target == t.target and time < worstStraightPath:
            worstStraightPath = time

    if len(argv) > 2:
        print("Worst time: %d" % worstStraightPath)

    mc = mcts.MCTS(TravelAgent(t, worstStraightPath), findOptimalSolution, C=C)

    if len(argv) > 2:
        print("Running simulations...")

    for i in range(TOTAL_ITERATIONS):
        if len(argv) > 2 and i % 100 == 0:
            print("Ran %d iterations" % i)
        mc.runSimulation()

    guess, foundSolution = mc.selectBestGuess()


    if argv[1] == "path":
        if not foundSolution or guess.traveller.timeElapsed > worstStraightPath:
            print("%d & 0.0" % worstStraightPath, end = " ")
        else:
            mean, var = byMean(guess)
            print("%.2f & %.2f" % (mean, var), end=" ")

    else: 
        report(mc)
    

if __name__ == "__main__":
    main()
