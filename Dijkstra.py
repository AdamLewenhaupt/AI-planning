import traveller
import map

class Dijkstra:
    """
    Implements Dijkstra's algorithm
    """

    def dijkstra(self, map, start_index, end_index):

        distance = []
        previous = []

        for i in range(len(map.walk)):
            distance[i] = float("inf")



def main():

    m = map.Map("./data/test/walk.mat", "./data/test/subway.mat", "./data/test/bus.mat")
    t = traveller.Traveller(m, 0)
    print(t)


if __name__ == "__main__":
    main()