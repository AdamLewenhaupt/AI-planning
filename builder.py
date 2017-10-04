from graph import Graph
from sys import argv

class Builder:
    """ 
    Further abstract Graph for our specific case.
    """

    walk = Graph()
    subway = Graph()
    bus = Graph()

    def addStation(self, name):
        self.walk.addNode(name)
        self.subway.addNode(name)
        self.bus.addNode(name)

    def canWalk(self, a, b, time):
        self.walk.join(a, b, time)

    def canTakeSubway(self, a, b, time):
        self.subway.join(a, b, time)

    def canTakeBus(self, a, b, time):
        self.bus.join(a, b, time)

def main():
    """Should be used to generate graphs for the .mat files
    From command line: python3 builder.py (walk|subway|bus)
    """

    b = Builder()

    # Trying to lay the map out sparsly to sort of convey distance in 1-D at least.
    b.addStation("Tekniska högskolan")

    b.addStation("Östermalmstorg")
    b.addStation("T-centralen")

    b.addStation("Slussen")

    # Adding walks. All have to be connnected.
    b.canWalk("T-centralen", "Tekniska högskolan", 40)
    b.canWalk("T-centralen", "Östermalmstorg", 25)
    b.canWalk("T-centralen", "Slussen", 30)

    b.canWalk("Östermalmstorg", "Tekniska högskolan", 30)
    b.canWalk("Östermalmstorg", "Slussen", 50)

    b.canWalk("Tekniska högskolan", "Slussen", 70)


    # Can walk between all nodes
    for i in range(len(b.walk.data)):
        for j in range(len(b.walk.data)):
            if i == j:
                continue
            assert(b.walk.data[i][j] == b.walk.data[j][i] and b.walk.data[i][j] > 0)

    if len(argv) < 2:
        print(b.walk.nameTable)
        return

    # Here our graph should be described.
    kind = argv[1] 

    if kind == "walk":
        print(b.walk)
    elif kind == "subway":
        print(b.subway)
    elif kind == "bus":
        print(b.bus)
    else:
        print("One of: walk, subway, bus")

if __name__ == "__main__":
    main()
