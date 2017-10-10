import mcts.mcts as mcts

from traveller import Traveller
from map import Map

C = 100
TOTAL_ITERATIONS = 1000
SHOWN = {}

def statistics(cond, data, x):
    h = hash(x)

    if h in data.keys():
        if not h in SHOWN.keys():
            print("%.2f %%, %.2f %%: %s" % (data[h] / cond[0] * 100, data[h] / TOTAL_ITERATIONS * 100, str(x)))
        SHOWN[h] = True
        cond[0] = data[h]

def report(mc):

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


def main():
    
    nameTable = {}

    with open("./data/test/register.json", encoding="UTF-8") as f:
        nameTable = eval(f.read())

    start = nameTable["Tekniska högskolan"]
    goal = nameTable["Slussen"]

    m = Map("./data/test/walk.mat", "./data/test/subway.mat", "./data/test/bus.mat")
    t = Traveller(m, start)
    t.setTarget(goal)

    worstStraightPath = 999999

    for (target, kind, time) in t.findLegalMoves():
        if target == t.target and time < worstStraightPath:
            worstStraightPath = time

    print("Worst time: %d" % worstStraightPath)

    mc = mcts.MCTS(TravelAgent(t, worstStraightPath), lambda solutions: min(solutions, key=lambda s: s.traveller.timeElapsed), C=C)

    print("Running simulations...")

    for i in range(TOTAL_ITERATIONS):
        if i % 100 == 0:
            print("Ran %d iterations" % i)
        mc.runSimulation()

    guess, foundSolution = mc.selectBestGuess()

    if not foundSolution or guess.traveller.timeElapsed > worstStraightPath:
        print("Just walk %d" % worstStraightPath)
    else:
        print("Path: %s, takes: %d" % (str(guess), guess.traveller.timeElapsed))

    report(mc)
    

if __name__ == "__main__":
    main()
