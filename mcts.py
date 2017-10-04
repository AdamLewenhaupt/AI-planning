import mcts.mcts as mcts

from traveller import Traveller
from map import Map

class TravelAgent(mcts.Agent):
    """ Provides an interface between the Traveller and the MCTS
    """

    def __init__(self, traveller, worstStraightPath):
        self.traveller = traveller
        self.worstStraightPath = worstStraightPath

    def findLegalNextStates(self):
        moves = self.traveller.findLegalMoves()
        travellers = [self.traveller.moveTo(move) for move in moves]
        return [TravelAgent(t, self.worstStraightPath) for t in travellers]
        
    def score(self):
        """
        We define the score as such: 1 - elapsed-time / worst-naive-time
        This gives a function that gives minus to times > worst-naive-time
        0 to equal times
        and + to better times
        """
        return 1 - (self.traveller.timeElapsed / self.worstStraightPath)

    def isDone(self):
        return self.traveller.isAtGoal()

    def __str__(self):
        return str(self.traveller)

def main():
    
    nameTable = {}

    with open("./data/test/register.json") as f:
        nameTable = eval(f.read())

    start = nameTable["Slussen"]
    goal = nameTable["Tekniska högskolan"]

    m = Map("./data/test/walk.mat", "./data/test/subway.mat", "./data/test/bus.mat")
    t = Traveller(m, start)
    t.setTarget(goal)

    worstStraightPath = 999999

    for (target, kind, time) in t.findLegalMoves():
        if target == t.target and time < worstStraightPath:
            worstStraightPath = time

    print("Worst time: %d" % worstStraightPath)


    mc = mcts.MCTS(TravelAgent(t, worstStraightPath))

    for i in range(1000):
        mc.runSimulation()

    print("Best guess:")
    guess, score = mc.selectBestGuess()
    print(str(guess), str(score))
    print(guess.traveller.timeElapsed)
    

if __name__ == "__main__":
    main()
