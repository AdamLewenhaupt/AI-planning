from traveller import Traveller
from map import Map

def main():
    nameTable = {}

    with open("./data/test/register.json") as f:
        nameTable = eval(f.read())

    start = nameTable["Mariatorget"]
    goal = nameTable["Tekniska högskolan"]

    m = Map("./data/test/walk.mat", "./data/test/subway.mat", "./data/test/bus.mat")
    t = Traveller(m, start)
    t.setTarget(goal)

    t1 = t.moveTo(t.findLegalMoves()[-1])
    print(t1.visited)
    print(t1, t1.timeElapsed)

    print(t1.currentNode)

    print(nameTable["Zinkensdamm"])
    print(nameTable["Mariatorget"], t1.currentNode, t1.findLegalMoves()[-1])
    t2 = t.moveTo(t1.findLegalMoves()[-1])
    print(t2, t2.timeElapsed)

    t3 = t2.moveTo(t2.findLegalMoves()[-1])
    print(t3, t3.timeElapsed)

    t4 = t3.moveTo(t3.findLegalMoves()[-1])
    print(t4, t4.timeElapsed)


if __name__ == "__main__":
    main()
