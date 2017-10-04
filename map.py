import numpy as np

WALK = 0
SUBWAY = 1
BUS = 2

class Map:
    """The map class handles to underlaying representation
    of all the travelling graphes and is responsible for
    simulating delays and calculate travelling times between
    nodes.
    """

    BUS_LEAVES_EVERY = 20
    SUBWAY_LEAVES_EVERY = 10

    # Considered as +x minutes
    BUS_ARRIVAL_VARIANCE = np.sqrt(5)
    SUBWAY_ARRIVAL_VARIANCE = np.sqrt(2)

    # Gives resonable values
    BUS_DELAY_VARIANCE = np.sqrt(0.5)
    SUBWAY_DELAY_VARIANCE = np.sqrt(0.2)

    def __init__(self, walk, subway, bus):
        """Initialize a new map
        :param walk: Path to .mat file for walking
        :param subway: Path to .mat file for subway
        :param bus: Path to .mat file for bus

        The files should have the format (example 2x3):
        1 2 3
        3 2 1
        """

        try:
            self.walk = np.loadtxt(walk)
            self.subway = np.loadtxt(subway)
            self.bus = np.loadtxt(bus)
        except Exception as e:
            raise e


        # Add if not zero.
        self.addNZ = np.vectorize(lambda x, y: x + y if x > 0 else x)


    def calculateScheduleDelay(self, time):
        """ Account for the time until the next bus / train leaves with variance.
        :param time: The current time in the simulation.
        """
        
        timeToNextBus = time % self.BUS_LEAVES_EVERY
        timeToNextSubway = time % self.SUBWAY_LEAVES_EVERY

        timeToNextBus += np.random.lognormal(sigma=self.BUS_ARRIVAL_VARIANCE)
        timeToNextSubway += np.random.lognormal(sigma=self.SUBWAY_ARRIVAL_VARIANCE)

        return timeToNextBus, timeToNextSubway


    def getMoves(self, currentNode, time):
        """Get all possible moves from the current node, with time of arrival
        if all stochastic elements are considered. Time is absolute based on the
        input time.

        :param currentNode: The index of our current node
        :param time: number of minutes that has passed

        :return: three numpy vectors: walk, subway, bus; with arrival times entered. 0 implies unreachable node.
        """
        
        timeToNextBus, timeToNextSubway = self.calculateScheduleDelay(time)

        # Retrieve possible paths from current node (creates copies)
        w = self.walk[:, currentNode]
        s = self.subway[:, currentNode]
        b = self.bus[:, currentNode]

        # apply variance.
        subwayVariance = np.random.normal(scale=self.SUBWAY_DELAY_VARIANCE, size=w.shape)
        busVariance = np.random.normal(scale=self.BUS_DELAY_VARIANCE, size=w.shape)

        s = np.multiply(s, 1 + subwayVariance)
        b = np.multiply(b, 1 + busVariance)

        s = self.addNZ(s, timeToNextSubway + time)
        b = self.addNZ(b, timeToNextBus + time)

        return w, s, b

def main():
    """
    Testing Map class
    """

    m = Map("./data/test/walk.mat", "./data/test/subway.mat", "./data/test/bus.mat")

    print(m.getMoves(0, 0))


if __name__ == "__main__":
    main()
