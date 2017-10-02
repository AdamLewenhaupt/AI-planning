import numpy as np
from map import Map, WALK, SUBWAY, BUS

transp = ["W", "S", "B"]

class Traveller:
    """Responsible for the state of the application.
    This class handles: finding valid moves from a node and
    making sure nodes are not being revisited.
    """

    def __init__(self, theMap, startAt):
        """Initialize a traveller
        :param theMap: An instance of the Map class
        :param startAt: The node index where the agent starts
        """
        self.currentNode = startAt
        self.map = theMap
        self.timeElapsed = 0
        self.lastVisited = -1
        self.history = []


    def createMoves(self, items, t):
        """Create a list of moves from the maps output.
        :param items: A numpy list of possible moves.
        :param t: the type of transportation.
        """

        return [(i,t,x) for (i,x) in enumerate(items.tolist()) if x > 0 and i != self.lastVisited]

    def findLegalMoves(self):
        """
        Find all available moves the map finds
        with the constraint that we don't go to
        our previous visited node.

        :return: All possible moves from the given state.
        """
        w, s, b = self.map.getMoves(self.currentNode, self.timeElapsed)

        return self.createMoves(w, WALK) + self.createMoves(s, SUBWAY) + self.createMoves(b, BUS)
        

    def moveTo(self, move):
        """
        Move the agent to the given node by the given means.
        The move is assumed to be legal.
        :param move: A valid move we wish to execute (node, transportation, timeAfter)
        :return: A new agent instance at the given node.
        """
        newAgent = Traveller(self.map, move[0])
        newAgent.lastVisited = self.currentNode
        newAgent.history.append((self.currentNode, move[1]))
        newAgent.history = newAgent.history + self.history
        newAgent.timeElapsed = move[2]

        return newAgent

    def __str__(self):
        """Convert to string"""
        return " ".join(["%d%s" % (n, transp[t]) for n,t in self.history])

def main():
    """Testing
    """

    m = Map("./walk.mat", "./subway.mat", "./bus.mat")
    t = Traveller(m, 0)

    moves = t.findLegalMoves()
    t1 = t.moveTo(moves[4])
    print(t1)
    print(t1.moveTo(t1.findLegalMoves()[0]))


if __name__ == "__main__":
    main()
