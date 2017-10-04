import random

class Agent:
    """
    General class that facilitates MCTS.
    Should be inherited as to provide an 
    interface to the MCTS algorithm.
    """

    def findLegalNextStates(self):
        """ Return all legal next states """
        raise Exception("Must be implemented")

    def isDone(self):
        """ Check wether we are done. """
        raise Exception("Must be implemented")

    def score(self):
        """ Calculate score at state. """
        raise Exception("Must be implemented")

class MCTS:
    """
    This class is responsible for executing monte-carlo simulations
    in order to find the optimal path selection.
    We only consider single-agent problems.
    """

    def __init__(self, agent, maxDepth = 4):
        """Initialize an MCTS
        :param agent: The agent whose path we will try to optimize
        :param maxDepth: The maximal depth that will be traversed

        :type agent: Agent
        """

        self.initialState = agent
        self.maxDepth = maxDepth

        self.counter = {}
        self.score = {}

    def getScore(self, h):
        """
        Determine the average score for a state.
        """
        return self.score[h] / self.counter[h]


    def runSimulation(self):
        """Run a Monte-Carlo simulation with the agent.
        """

        hasExpanded = False
        currentState = self.initialState
        visited = []

        for i in range(self.maxDepth):

            currentState = random.choice(currentState.findLegalNextStates())

            if currentState.isDone():
                break

            h = str(currentState)

            if not hasExpanded:
                if not h in self.counter.keys():
                    hasExpanded = True
                    self.counter[h] = 0
                    self.score[h] = 0

                visited.append(h)

        score = currentState.score()
        for h in visited:
            self.counter[h] += 1
            self.score[h] += score


    def selectBestGuess(self):
        """Select the path which we currently approximate to give the best score.
        """

        currentState = self.initialState 

        while not currentState.isDone():
            possibleNextStates = [(s, self.getScore(str(s))) for s in currentState.findLegalNextStates() if str(s) in self.counter]

            if len(possibleNextStates) == 0:
                break

            bestOption = max(possibleNextStates, key=lambda x: x[1])
            currentState = bestOption[0]

        return currentState, bestOption[1]
