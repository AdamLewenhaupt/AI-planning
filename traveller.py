import numpy as np
from map import Map, WALK, SUBWAY, BUS

TRANSPORTATIONS = ["walk", "subway", "bus"]

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
        self.target = -1


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
        newAgent.target = self.target
        newAgent.lastVisited = self.currentNode
        newAgent.history.append((self.currentNode, move[1]))
        newAgent.history = newAgent.history + self.history
        newAgent.timeElapsed = move[2]

        return newAgent

    def setTarget(self, node):
        self.target = node

    def isAtGoal(self):
        return self.currentNode == self.target

    def __str__(self):
        """Convert to string"""
        reversed_hist = list(reversed(self.history))
        #print(reversed_hist)
        if self.isAtGoal():
            return " ".join(["%d -> %s ->" % (n, TRANSPORTATIONS[t]) for n,t in reversed_hist]) + " " + str(self.currentNode)
        else:
            return " ".join(["%d %s ->" % (n, TRANSPORTATIONS[t]) for n,t in reversed_hist])


def main():
    """Testing
    """

    m = Map("./data/test/walk.mat", "./data/test/subway.mat", "./data/test/bus.mat")
    t = Traveller(m, 0)

    moves = t.findLegalMoves()
    print(moves[4])
    t1 = t.moveTo(moves[4])
    print(t1)
    print(t1.moveTo(t1.findLegalMoves()[0]))


if __name__ == "__main__":
    main()
