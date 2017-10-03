import mcts.mcts as mcts

from traveller import Traveller
from map import Map

class TravelAgent(mcts.Agent):
    """ Provides an interface between the Traveller and the MCTS
    """

    def __init__(self, traveller):
        self.traveller = traveller

    def findLegalNextStates(self):
        moves = self.traveller.findLegalMoves()
        travellers = [self.traveller.moveTo(move) for move in moves]
        return [TravelAgent(t) for t in travellers]
        
    def score(self):
        return 1 / self.traveller.timeElapsed

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

    mc = mcts.MCTS(TravelAgent(t))

    for i in range(1000):
        mc.runSimulation()

    print(mc.counter)
    guess, score = mc.selectBestGuess()
    print(str(guess), str(score))
    print(guess.traveller.timeElapsed)
    

if __name__ == "__main__":
    main()
