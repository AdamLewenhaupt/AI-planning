import numpy as np
from map import Map, WALK, SUBWAY, BUS
import statistics

# A bit dirty, but works for now.
NAME_TABLE = None
with open("./data/test/register.json", encoding="UTF-8") as f:
    NAME_TABLE = eval(f.read())

NAME_TABLE = {v: k for k, v in NAME_TABLE.items()}

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
        self.visited = []
        self.target = -1


    def createMoves(self, items, t):
        """Create a list of moves from the maps output.
        :param items: A list of possible moves.
        :param t: the type of transportation.
        :return: A list of (index, transport, time)
        """
        return [(i,t,x) for (i,x) in enumerate(items) if x > 0 and not i in self.visited]

    def findLegalMoves(self):
        """
        Find all available moves the map finds
        with the constraint that we don't go to
        our previously visited nodes.

        :return: All possible moves from the given state.
        """

        currentlyUsing = -1
        if len(self.history) > 0:
            currentlyUsing = self.history[-1][1]

        w, s, b = self.map.getMoves(self.currentNode, self.timeElapsed, currentlyUsing)

        return self.createMoves(w, WALK) + self.createMoves(s, SUBWAY) + self.createMoves(b, BUS)
        

    def moveTo(self, move):
        """
        Move the agent to the given node by the given means.
        The move is assumed to be legal.
        :param move: A valid move we wish to execute (node, transportation, timeElapsed)
        :return: A new agent instance at the given node.
        """
        
        newAgent = Traveller(self.map, move[0])
        newAgent.target = self.target
        newAgent.lastVisited = self.currentNode
        newAgent.history.append((self.currentNode, move[1]))
        newAgent.history = newAgent.history + self.history
        newAgent.visited = [x[0] for x in newAgent.history]
        newAgent.timeElapsed = move[2] + self.timeElapsed

        return newAgent

    def setTarget(self, node):
        self.target = node

    def isAtGoal(self):
        return self.currentNode == self.target

    def __str__(self):
        """Convert to string"""
        reversed_hist = list(reversed(self.history))
        return " ".join(["%s -> %s ->" % (NAME_TABLE[n], TRANSPORTATIONS[t]) for n,t in reversed_hist]) + " " + NAME_TABLE[self.currentNode]


    def __hash__(self):
        return hash(tuple(self.history))


    def rewalk(self, fn):
        """ Rewalk path and do something at every timestep.
        :param fn: A function to execute at every timestep. Takes the state as arg.
        """

        initialNode = self.visited[-1]
        t = Traveller(self.map, initialNode)
        t.setTarget(self.target)

        fn(t)

        for i in reversed(range(len(self.visited) - 1)):


            kind = self.history[i + 1][1]

            moves = t.findLegalMoves()

            m = filter(lambda x: x[0] == self.visited[i] and x[1] == kind, moves)
            m = list(m)

            if len(m) == 0:
                return
            
            t = t.moveTo(m[0])

            fn(t)

    
        moves = t.findLegalMoves()
        kind = self.history[0][1]
        m = filter(lambda x: x[0] == self.currentNode and x[1] == kind, moves)
        m = list(m)

        if len(m) == 0:
            return
        
        t = t.moveTo(m[0])
        fn(t)


    def _add(self, result, state):
        if state.isAtGoal():
            result.append(state.timeElapsed)

    def simulate(self, N = 1000):
        """ Simulate the path to get statistics on travel times.
        :param N: The amount of samples to draw
        """

        data = []


        for i in range(N):
            self.rewalk(lambda s: self._add(data, s))

        mean = statistics.mean(data)
        return mean, statistics.variance(data, mean)



def main():
    """ Testing """


    print("Simulation")

    m = Map("./data/test/walk.mat", "./data/test/subway.mat", "./data/test/bus.mat")
    t = Traveller(m, 3)
    t.setTarget(0)

    moves = t.findLegalMoves()

    print(moves[1])
    t1 = t.moveTo(moves[2])
    print(t1)
    print(t1.timeElapsed)

    t2 = t1.moveTo(t1.findLegalMoves()[-1])
    print(t2)
    print(t2.timeElapsed)

    print(t2.isAtGoal())

    t3 = t2.moveTo(t2.findLegalMoves()[0])
    print(t3)
    print(t3.timeElapsed)

    print(t3.currentNode)

    print(t3.isAtGoal())
    print(t3.timeElapsed)

    print("Rewalk")
    t3.rewalk(lambda x: print(x))

    
    mean, var = t3.simulate(1000)
    print(mean, var)
    

if __name__ == "__main__":
    main()
