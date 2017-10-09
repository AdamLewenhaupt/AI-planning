import random
import math

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


    def __init__(self, agent, heuristic, maxDepth = 40, C = 10):
        """Initialize an MCTS
        :param agent: The agent whose path we will try to optimize
        :param heuristic: A function for selecting among candidate paths
        :param maxDepth: The maximal depth that will be traversed

        :type agent: Agent
        """

        self.C = C
        self.heuristic = heuristic
        self.initialState = agent
        self.maxDepth = maxDepth

        self.counter = {}
        self.score = {}

    def getScore(self, h):
        """
        Determine the average score for a state.
        """
        return self.score[h] / self.counter[h]

    def ucb(self, states):

        keys = self.counter.keys()
        maxScore = -9999
        best = 0
        n = 0

        hashes = [hash(s) for s in states]

        for s in hashes:
            if s in keys:
                n += self.counter[s]
            else:
                return random.choice(states)

        for s in hashes:
            score = self.getScore(s)
            score += self.C * math.sqrt(math.log(n) / self.counter[s])
            if score > maxScore:
                maxScore = score
                best = s

        return states[hashes.index(best)]

    def runSimulation(self):
        """Run a Monte-Carlo simulation with the agent.
        """

        hasExpanded = False
        currentState = self.initialState
        visited = []

        for i in range(self.maxDepth):

            nextStates = currentState.findLegalNextStates()

            if len(nextStates) == 0:
                break

            elif len(nextStates) == 1:
                currentState = nextStates[0]
            else:
                currentState = self.ucb(nextStates)

            h = hash(currentState)

            if not hasExpanded:
                if not h in self.counter.keys():
                    hasExpanded = True
                    self.counter[h] = 0
                    self.score[h] = 0
                
                visited.append(h)

            if currentState.isDone():
                break

        score = currentState.score()
        for h in visited:
            self.counter[h] += 1
            self.score[h] += score


    def findSolutions(self, state, c):
        """
        Parse our results into solutions.
        :param state: The state to start from
        :param c: list to accumulate solutions into
        :return: nothing.
        """

        if state.isDone():
            c.append(state)

        # Filter available options.
        for s in state.findLegalNextStates():
            h = hash(s)
            if h in self.counter.keys() and self.getScore(h) > 0:
                prob = self.getScore(h)
                self.findSolutions(s, c)


    def selectBestGuess(self):
        """Select the path which we currently approximate to give the best score.
        :return: The best solution, wether a solution was found.
        """

        solutions = []
        self.findSolutions(self.initialState, solutions)

        if len(solutions) > 0:
            return self.heuristic(solutions), True
        else:
            return None, False


