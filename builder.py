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
    
    b.addStation("Slussen")
    b.addStation("Gamla stan")
    b.addStation("T-centralen")
    b.addStation("Hötorget")
    b.addStation("Rådmansgatan")
    b.addStation("Odenplan")
    b.addStation("S:t Eriksplan")
    b.addStation("Kungsholmen")
    b.addStation("Tekniska högskolan")
    b.addStation("Stadion")
    b.addStation("Östermalmstorg")
    b.addStation("Mariatorget")
    b.addStation("Zinkensdamm")
    b.addStation("Odengatan")
    b.addStation("Vasaparken")
    b.addStation("Norrtull")
    b.addStation("Eriksbergsgatan")
    b.addStation("Kungsträdgården")
    b.addStation("Slottet")

    # Adding subways. 
    # Red line
    b.canTakeSubway("Stadion", "Tekniska högskolan", 3 )
    b.canTakeSubway("Tekniska högskolan", "Östermalmstorg", 5)
    b.canTakeSubway("Östermalmstorg", "T-centralen", 4)
    b.canTakeSubway("T-centralen", "Gamla stan", 7)         # ALSO GREEN LINE
    b.canTakeSubway("Gamla stan", "Slussen", 2)             # ALSO GREEN LINE
    b.canTakeSubway("Slussen", "Mariatorget", 6)
    b.canTakeSubway("Mariatorget", "Zinkensdamm", 9)

    # Green line
    b.canTakeSubway("T-centralen", "Hötorget", 5)
    b.canTakeSubway("Hötorget", "Rådmansgatan", 2)
    b.canTakeSubway("Rådmansgatan", "Odenplan", 3)
    b.canTakeSubway("Odenplan", "S:t Eriksplan", 4)
    b.canTakeSubway("S:t Eriksplan", "Kungsholmen", 7)


    # Adding busses.
    # 2
    b.canTakeBus("Norrtull", "Odenplan", 5)
    b.canTakeBus("Odenplan", "Eriksbergsgatan", 9)
    b.canTakeBus("Eriksbergsgatan", "Östermalmstorg", 6)
    b.canTakeBus("Östermalmstorg", "Kungsträdgården", 11)
    b.canTakeBus("Kungsträdgården", "Slottet", 8)

    # 4
    b.canTakeBus("Stadion", "Tekniska högskolan", 4)
    b.canTakeBus("Tekniska högskolan", "Odengatan", 6)
    b.canTakeBus("Odengatan", "Odenplan", 7)
    b.canTakeBus("Odenplan", "Vasaparken", 3)
    b.canTakeBus("Vasaparken", "S:t Eriksplan", 3)
    b.canTakeBus("S:t Eriksplan", "Kungsholmen", 4)


    # Adding walks. All have to be connnected.

    # Gå från Slussen till VART DU VILL...
    b.canWalk("Slussen", "Gamla stan", 15)
    b.canWalk("Slussen", "T-centralen", 20)
    b.canWalk("Slussen", "Hötorget", 30)
    b.canWalk("Slussen", "Rådmansgatan", 37)
    b.canWalk("Slussen", "Odenplan", 42)
    b.canWalk("Slussen", "S:t Eriksplan", 49)
    b.canWalk("Slussen", "Kungsholmen", 40)
    b.canWalk("Slussen", "Tekniska högskolan", 35)
    b.canWalk("Slussen", "Stadion", 31)
    b.canWalk("Slussen", "Östermalmstorg", 24)
    b.canWalk("Slussen", "Mariatorget", 17)
    b.canWalk("Slussen", "Zinkensdamm", 23)
    b.canWalk("Slussen", "Odengatan", 40)
    b.canWalk("Slussen", "Vasaparken", 46)
    b.canWalk("Slussen", "Norrtull", 46)
    b.canWalk("Slussen", "Eriksbergsgatan", 28)
    b.canWalk("Slussen", "Kungsträdgården", 14)
    b.canWalk("Slussen", "Slottet", 9)


  # Gå från Gamla stan till VART DU VILL...
    b.canWalk("Gamla stan", "T-centralen", 15)
    b.canWalk("Gamla stan", "Hötorget", 25)
    b.canWalk("Gamla stan", "Rådmansgatan", 29)
    b.canWalk("Gamla stan", "Odenplan", 34)
    b.canWalk("Gamla stan", "S:t Eriksplan", 40)
    b.canWalk("Gamla stan", "Kungsholmen", 46)
    b.canWalk("Gamla stan", "Tekniska högskolan", 28)
    b.canWalk("Gamla stan", "Stadion", 26)
    b.canWalk("Gamla stan", "Östermalmstorg", 16)
    b.canWalk("Gamla stan", "Mariatorget", 24)
    b.canWalk("Gamla stan", "Zinkensdamm", 29)
    b.canWalk("Gamla stan", "Odengatan", 30)
    b.canWalk("Gamla stan", "Vasaparken", 37)
    b.canWalk("Gamla stan", "Norrtull", 37)
    b.canWalk("Gamla stan", "Eriksbergsgatan", 21)
    b.canWalk("Gamla stan", "Kungsträdgården", 8)
    b.canWalk("Gamla stan", "Slottet", 4)

    # Gå från T-centralen till VART DU VILL...
    b.canWalk("T-centralen", "Hötorget", 11)
    b.canWalk("T-centralen", "Rådmansgatan", 14)
    b.canWalk("T-centralen", "Odenplan", 13)
    b.canWalk("T-centralen", "S:t Eriksplan", 18)
    b.canWalk("T-centralen", "Kungsholmen", 13)
    b.canWalk("T-centralen", "Tekniska högskolan", 25)
    b.canWalk("T-centralen", "Stadion", 28)
    b.canWalk("T-centralen", "Östermalmstorg", 20)
    b.canWalk("T-centralen", "Mariatorget", 26)
    b.canWalk("T-centralen", "Zinkensdamm", 31)
    b.canWalk("T-centralen", "Odengatan", 12)
    b.canWalk("T-centralen", "Vasaparken", 17)
    b.canWalk("T-centralen", "Norrtull", 18)
    b.canWalk("T-centralen", "Eriksbergsgatan", 24)
    b.canWalk("T-centralen", "Kungsträdgården", 11)
    b.canWalk("T-centralen", "Slottet", 15)

    # Gå från Hötorget till VART DU VILL...
    b.canWalk("Hötorget", "Rådmansgatan", 7)
    b.canWalk("Hötorget", "Odenplan", 13)
    b.canWalk("Hötorget", "S:t Eriksplan", 22)
    b.canWalk("Hötorget", "Kungsholmen", 18)
    b.canWalk("Hötorget", "Tekniska högskolan", 19)
    b.canWalk("Hötorget", "Stadion", 23)
    b.canWalk("Hötorget", "Östermalmstorg", 13)
    b.canWalk("Hötorget", "Mariatorget", 30)
    b.canWalk("Hötorget", "Zinkensdamm", 37)
    b.canWalk("Hötorget", "Odengatan", 11)
    b.canWalk("Hötorget", "Vasaparken", 14)
    b.canWalk("Hötorget", "Norrtull", 18)
    b.canWalk("Hötorget", "Eriksbergsgatan", 17)
    b.canWalk("Hötorget", "Kungsträdgården", 15)
    b.canWalk("Hötorget", "Slottet", 18)

    # Gå från Rådmansgatan till VART DU VILL...
    b.canWalk("Rådmansgatan", "Odenplan", 8)
    b.canWalk("Rådmansgatan", "S:t Eriksplan", 18)
    b.canWalk("Rådmansgatan", "Kungsholmen", 18)
    b.canWalk("Rådmansgatan", "Tekniska högskolan", 15)
    b.canWalk("Rådmansgatan", "Stadion", 19)
    b.canWalk("Rådmansgatan", "Östermalmstorg", 14)
    b.canWalk("Rådmansgatan", "Mariatorget", 28)
    b.canWalk("Rådmansgatan", "Zinkensdamm", 36)
    b.canWalk("Rådmansgatan", "Odengatan", 7)
    b.canWalk("Rådmansgatan", "Vasaparken", 12)
    b.canWalk("Rådmansgatan", "Norrtull", 12)
    b.canWalk("Rådmansgatan", "Eriksbergsgatan", 11)
    b.canWalk("Rådmansgatan", "Kungsträdgården", 18)
    b.canWalk("Rådmansgatan", "Slottet", 21)

    # Gå från Odenplan till VART DU VILL...
    b.canWalk("Odenplan", "S:t Eriksplan", 7)
    b.canWalk("Odenplan", "Kungsholmen", 15)
    b.canWalk("Odenplan", "Tekniska högskolan", 12)
    b.canWalk("Odenplan", "Stadion", 16)
    b.canWalk("Odenplan", "Östermalmstorg", 16)
    b.canWalk("Odenplan", "Mariatorget", 33)
    b.canWalk("Odenplan", "Zinkensdamm", 37)
    b.canWalk("Odenplan", "Odengatan", 3)
    b.canWalk("Odenplan", "Vasaparken", 4)
    b.canWalk("Odenplan", "Norrtull", 3)
    b.canWalk("Odenplan", "Eriksbergsgatan", 12)
    b.canWalk("Odenplan", "Kungsträdgården", 16)
    b.canWalk("Odenplan", "Slottet", 21)

    # Gå från S:t Eriksplan till VART DU VILL...
    b.canWalk("S:t Eriksplan", "Kungsholmen", 8)
    b.canWalk("S:t Eriksplan", "Tekniska högskolan", 16)
    b.canWalk("S:t Eriksplan", "Stadion", 21)
    b.canWalk("S:t Eriksplan", "Östermalmstorg", 21)
    b.canWalk("S:t Eriksplan", "Mariatorget", 30)
    b.canWalk("S:t Eriksplan", "Zinkensdamm", 22)
    b.canWalk("S:t Eriksplan", "Odengatan", 7)
    b.canWalk("S:t Eriksplan", "Vasaparken", 3)
    b.canWalk("S:t Eriksplan", "Norrtull", 12)
    b.canWalk("S:t Eriksplan", "Eriksbergsgatan", 19)
    b.canWalk("S:t Eriksplan", "Kungsträdgården", 21)
    b.canWalk("S:t Eriksplan", "Slottet", 26)

    # Gå från Kungsholmen till VART DU VILL...
    b.canWalk("Kungsholmen", "Tekniska högskolan", 25)
    b.canWalk("Kungsholmen", "Stadion", 29)
    b.canWalk("Kungsholmen", "Östermalmstorg", 21)
    b.canWalk("Kungsholmen", "Mariatorget", 29)
    b.canWalk("Kungsholmen", "Zinkensdamm", 25)
    b.canWalk("Kungsholmen", "Odengatan", 17)
    b.canWalk("Kungsholmen", "Vasaparken", 14)
    b.canWalk("Kungsholmen", "Norrtull", 19)
    b.canWalk("Kungsholmen", "Eriksbergsgatan", 21)
    b.canWalk("Kungsholmen", "Kungsträdgården", 24)
    b.canWalk("Kungsholmen", "Slottet", 28)

    # Gå från Tekniska högskolan till VART DU VILL...
    b.canWalk("Tekniska högskolan", "Stadion", 3)
    b.canWalk("Tekniska högskolan", "Östermalmstorg", 14)
    b.canWalk("Tekniska högskolan", "Mariatorget", 32)
    b.canWalk("Tekniska högskolan", "Zinkensdamm", 39)
    b.canWalk("Tekniska högskolan", "Odengatan", 8)
    b.canWalk("Tekniska högskolan", "Vasaparken", 16)
    b.canWalk("Tekniska högskolan", "Norrtull", 16)
    b.canWalk("Tekniska högskolan", "Eriksbergsgatan", 16)
    b.canWalk("Tekniska högskolan", "Kungsträdgården", 28)
    b.canWalk("Tekniska högskolan", "Slottet", 34)

    # Gå från Stadion till VART DU VILL...
    b.canWalk("Stadion", "Östermalmstorg", 11)
    b.canWalk("Stadion", "Mariatorget", 29)
    b.canWalk("Stadion", "Zinkensdamm", 37)
    b.canWalk("Stadion", "Odengatan", 12)
    b.canWalk("Stadion", "Vasaparken", 19)
    b.canWalk("Stadion", "Norrtull", 19)
    b.canWalk("Stadion", "Eriksbergsgatan", 21)
    b.canWalk("Stadion", "Kungsträdgården", 26)
    b.canWalk("Stadion", "Slottet", 31)

    # Gå från Östermalmstorg till VART DU VILL...
    b.canWalk("Östermalmstorg", "Mariatorget", 24)
    b.canWalk("Östermalmstorg", "Zinkensdamm", 31)
    b.canWalk("Östermalmstorg", "Odengatan", 16)
    b.canWalk("Östermalmstorg", "Vasaparken", 16)
    b.canWalk("Östermalmstorg", "Norrtull", 19)
    b.canWalk("Östermalmstorg", "Eriksbergsgatan", 5)
    b.canWalk("Östermalmstorg", "Kungsträdgården", 15)
    b.canWalk("Östermalmstorg", "Slottet", 19)

    # Gå från Mariatorget till VART DU VILL...
    b.canWalk("Mariatorget", "Zinkensdamm", 8)
    b.canWalk("Mariatorget", "Odengatan", 28)
    b.canWalk("Mariatorget", "Vasaparken", 25)
    b.canWalk("Mariatorget", "Norrtull", 30)
    b.canWalk("Mariatorget", "Eriksbergsgatan", 17)
    b.canWalk("Mariatorget", "Kungsträdgården", 15)
    b.canWalk("Mariatorget", "Slottet", 11)

    # Gå från Zinkensdamm till VART DU VILL...
    b.canWalk("Zinkensdamm", "Odengatan", 32)
    b.canWalk("Zinkensdamm", "Vasaparken", 29)
    b.canWalk("Zinkensdamm", "Norrtull", 34)
    b.canWalk("Zinkensdamm", "Eriksbergsgatan", 18)
    b.canWalk("Zinkensdamm", "Kungsträdgården", 20)
    b.canWalk("Zinkensdamm", "Slottet", 15)
  
    # Gå från Odengatan till VART DU VILL...
    b.canWalk("Odengatan", "Vasaparken", 9)
    b.canWalk("Odengatan", "Norrtull", 6)
    b.canWalk("Odengatan", "Eriksbergsgatan", 7)
    b.canWalk("Odengatan", "Kungsträdgården", 21)
    b.canWalk("Odengatan", "Slottet", 26)

    # Gå från Vasaparken till VART DU VILL...
    b.canWalk("Vasaparken", "Norrtull", 6)
    b.canWalk("Vasaparken", "Eriksbergsgatan", 14)
    b.canWalk("Vasaparken", "Kungsträdgården", 21)
    b.canWalk("Vasaparken", "Slottet", 28)

    # Gå från Norrtull till VART DU VILL...
    b.canWalk("Norrtull", "Eriksbergsgatan", 12)
    b.canWalk("Norrtull", "Kungsträdgården", 26)
    b.canWalk("Norrtull", "Slottet", 31)

    # Gå från Eriksbergsgatan till VART DU VILL...
    b.canWalk("Eriksbergsgatan", "Kungsträdgården", 18)
    b.canWalk("Eriksbergsgatan", "Slottet", 25)

    # Gå från Kungsträdgården till VART DU VILL...
    b.canWalk("Kungsträdgården", "Slottet", 6)



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

