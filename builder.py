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
    From command line: python8 builder.py (walk|subway|bus)
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
    b.canTakeSubway("Stadion", "Östermalmstorg", 5)
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
    b.canWalk("Slussen", "Gamla stan", 30)
    b.canWalk("Slussen", "T-centralen", 35)
    b.canWalk("Slussen", "Hötorget", 45)
    b.canWalk("Slussen", "Rådmansgatan", 52)
    b.canWalk("Slussen", "Odenplan", 57)
    b.canWalk("Slussen", "S:t Eriksplan", 64)
    b.canWalk("Slussen", "Kungsholmen", 55)
    b.canWalk("Slussen", "Tekniska högskolan", 50)
    b.canWalk("Slussen", "Stadion", 41)
    b.canWalk("Slussen", "Östermalmstorg", 34)
    b.canWalk("Slussen", "Mariatorget", 27)
    b.canWalk("Slussen", "Zinkensdamm", 33)
    b.canWalk("Slussen", "Odengatan", 50)
    b.canWalk("Slussen", "Vasaparken", 51)
    b.canWalk("Slussen", "Norrtull", 56)
    b.canWalk("Slussen", "Eriksbergsgatan", 38)
    b.canWalk("Slussen", "Kungsträdgården", 24)
    b.canWalk("Slussen", "Slottet", 19)


  # Gå från Gamla stan till VART DU VILL...
    b.canWalk("Gamla stan", "T-centralen", 25)
    b.canWalk("Gamla stan", "Hötorget", 35)
    b.canWalk("Gamla stan", "Rådmansgatan", 39)
    b.canWalk("Gamla stan", "Odenplan", 44)
    b.canWalk("Gamla stan", "S:t Eriksplan", 50)
    b.canWalk("Gamla stan", "Kungsholmen", 56)
    b.canWalk("Gamla stan", "Tekniska högskolan", 38)
    b.canWalk("Gamla stan", "Stadion", 36)
    b.canWalk("Gamla stan", "Östermalmstorg", 26)
    b.canWalk("Gamla stan", "Mariatorget", 34)
    b.canWalk("Gamla stan", "Zinkensdamm", 39)
    b.canWalk("Gamla stan", "Odengatan", 40)
    b.canWalk("Gamla stan", "Vasaparken", 47)
    b.canWalk("Gamla stan", "Norrtull", 47)
    b.canWalk("Gamla stan", "Eriksbergsgatan", 31)
    b.canWalk("Gamla stan", "Kungsträdgården", 18)
    b.canWalk("Gamla stan", "Slottet", 14)

    # Gå från T-centralen till VART DU VILL...
    b.canWalk("T-centralen", "Hötorget", 21)
    b.canWalk("T-centralen", "Rådmansgatan", 24)
    b.canWalk("T-centralen", "Odenplan", 23)
    b.canWalk("T-centralen", "S:t Eriksplan", 28)
    b.canWalk("T-centralen", "Kungsholmen", 23)
    b.canWalk("T-centralen", "Tekniska högskolan", 35)
    b.canWalk("T-centralen", "Stadion", 38)
    b.canWalk("T-centralen", "Östermalmstorg", 30)
    b.canWalk("T-centralen", "Mariatorget", 36)
    b.canWalk("T-centralen", "Zinkensdamm", 36)
    b.canWalk("T-centralen", "Odengatan", 22)
    b.canWalk("T-centralen", "Vasaparken", 27)
    b.canWalk("T-centralen", "Norrtull", 28)
    b.canWalk("T-centralen", "Eriksbergsgatan", 34)
    b.canWalk("T-centralen", "Kungsträdgården", 21)
    b.canWalk("T-centralen", "Slottet", 25)

    # Gå från Hötorget till VART DU VILL...
    b.canWalk("Hötorget", "Rådmansgatan", 17)
    b.canWalk("Hötorget", "Odenplan", 23)
    b.canWalk("Hötorget", "S:t Eriksplan", 32)
    b.canWalk("Hötorget", "Kungsholmen", 28)
    b.canWalk("Hötorget", "Tekniska högskolan", 29)
    b.canWalk("Hötorget", "Stadion", 33)
    b.canWalk("Hötorget", "Östermalmstorg", 23)
    b.canWalk("Hötorget", "Mariatorget", 40)
    b.canWalk("Hötorget", "Zinkensdamm", 47)
    b.canWalk("Hötorget", "Odengatan", 21)
    b.canWalk("Hötorget", "Vasaparken", 24)
    b.canWalk("Hötorget", "Norrtull", 28)
    b.canWalk("Hötorget", "Eriksbergsgatan", 27)
    b.canWalk("Hötorget", "Kungsträdgården", 25)
    b.canWalk("Hötorget", "Slottet", 28)

    # Gå från Rådmansgatan till VART DU VILL...
    b.canWalk("Rådmansgatan", "Odenplan", 18)
    b.canWalk("Rådmansgatan", "S:t Eriksplan", 28)
    b.canWalk("Rådmansgatan", "Kungsholmen", 28)
    b.canWalk("Rådmansgatan", "Tekniska högskolan", 25)
    b.canWalk("Rådmansgatan", "Stadion", 29)
    b.canWalk("Rådmansgatan", "Östermalmstorg", 24)
    b.canWalk("Rådmansgatan", "Mariatorget", 38)
    b.canWalk("Rådmansgatan", "Zinkensdamm", 46)
    b.canWalk("Rådmansgatan", "Odengatan", 22)
    b.canWalk("Rådmansgatan", "Vasaparken", 22)
    b.canWalk("Rådmansgatan", "Norrtull", 22)
    b.canWalk("Rådmansgatan", "Eriksbergsgatan", 21)
    b.canWalk("Rådmansgatan", "Kungsträdgården", 28)
    b.canWalk("Rådmansgatan", "Slottet", 31)

    # Gå från Odenplan till VART DU VILL...
    b.canWalk("Odenplan", "S:t Eriksplan", 17)
    b.canWalk("Odenplan", "Kungsholmen", 25)
    b.canWalk("Odenplan", "Tekniska högskolan", 22)
    b.canWalk("Odenplan", "Stadion", 26)
    b.canWalk("Odenplan", "Östermalmstorg", 26)
    b.canWalk("Odenplan", "Mariatorget", 43)
    b.canWalk("Odenplan", "Zinkensdamm", 47)
    b.canWalk("Odenplan", "Odengatan", 13)
    b.canWalk("Odenplan", "Vasaparken", 14)
    b.canWalk("Odenplan", "Norrtull", 13)
    b.canWalk("Odenplan", "Eriksbergsgatan", 22)
    b.canWalk("Odenplan", "Kungsträdgården", 26)
    b.canWalk("Odenplan", "Slottet", 31)

    # Gå från S:t Eriksplan till VART DU VILL...
    b.canWalk("S:t Eriksplan", "Kungsholmen", 18)
    b.canWalk("S:t Eriksplan", "Tekniska högskolan", 26)
    b.canWalk("S:t Eriksplan", "Stadion", 31)
    b.canWalk("S:t Eriksplan", "Östermalmstorg", 31)
    b.canWalk("S:t Eriksplan", "Mariatorget", 40)
    b.canWalk("S:t Eriksplan", "Zinkensdamm", 32)
    b.canWalk("S:t Eriksplan", "Odengatan", 17)
    b.canWalk("S:t Eriksplan", "Vasaparken", 13)
    b.canWalk("S:t Eriksplan", "Norrtull", 22)
    b.canWalk("S:t Eriksplan", "Eriksbergsgatan", 29)
    b.canWalk("S:t Eriksplan", "Kungsträdgården", 31)
    b.canWalk("S:t Eriksplan", "Slottet", 36)

    # Gå från Kungsholmen till VART DU VILL...
    b.canWalk("Kungsholmen", "Tekniska högskolan", 35)
    b.canWalk("Kungsholmen", "Stadion", 39)
    b.canWalk("Kungsholmen", "Östermalmstorg", 31)
    b.canWalk("Kungsholmen", "Mariatorget", 39)
    b.canWalk("Kungsholmen", "Zinkensdamm", 35)
    b.canWalk("Kungsholmen", "Odengatan", 27)
    b.canWalk("Kungsholmen", "Vasaparken", 24)
    b.canWalk("Kungsholmen", "Norrtull", 29)
    b.canWalk("Kungsholmen", "Eriksbergsgatan", 31)
    b.canWalk("Kungsholmen", "Kungsträdgården", 34)
    b.canWalk("Kungsholmen", "Slottet", 38)

    # Gå från Tekniska högskolan till VART DU VILL...
    b.canWalk("Tekniska högskolan", "Stadion", 13)
    b.canWalk("Tekniska högskolan", "Östermalmstorg", 24)
    b.canWalk("Tekniska högskolan", "Mariatorget", 42)
    b.canWalk("Tekniska högskolan", "Zinkensdamm", 49)
    b.canWalk("Tekniska högskolan", "Odengatan", 18)
    b.canWalk("Tekniska högskolan", "Vasaparken", 26)
    b.canWalk("Tekniska högskolan", "Norrtull", 26)
    b.canWalk("Tekniska högskolan", "Eriksbergsgatan", 26)
    b.canWalk("Tekniska högskolan", "Kungsträdgården", 38)
    b.canWalk("Tekniska högskolan", "Slottet", 44)

    # Gå från Stadion till VART DU VILL...
    b.canWalk("Stadion", "Östermalmstorg", 21)
    b.canWalk("Stadion", "Mariatorget", 39)
    b.canWalk("Stadion", "Zinkensdamm", 47)
    b.canWalk("Stadion", "Odengatan", 22)
    b.canWalk("Stadion", "Vasaparken", 29)
    b.canWalk("Stadion", "Norrtull", 29)
    b.canWalk("Stadion", "Eriksbergsgatan", 31)
    b.canWalk("Stadion", "Kungsträdgården", 36)
    b.canWalk("Stadion", "Slottet", 41)

    # Gå från Östermalmstorg till VART DU VILL...
    b.canWalk("Östermalmstorg", "Mariatorget", 34)
    b.canWalk("Östermalmstorg", "Zinkensdamm", 41)
    b.canWalk("Östermalmstorg", "Odengatan", 26)
    b.canWalk("Östermalmstorg", "Vasaparken", 26)
    b.canWalk("Östermalmstorg", "Norrtull", 29)
    b.canWalk("Östermalmstorg", "Eriksbergsgatan", 15)
    b.canWalk("Östermalmstorg", "Kungsträdgården", 25)
    b.canWalk("Östermalmstorg", "Slottet", 29)

    # Gå från Mariatorget till VART DU VILL...
    b.canWalk("Mariatorget", "Zinkensdamm", 18)
    b.canWalk("Mariatorget", "Odengatan", 38)
    b.canWalk("Mariatorget", "Vasaparken", 35)
    b.canWalk("Mariatorget", "Norrtull", 40)
    b.canWalk("Mariatorget", "Eriksbergsgatan", 27)
    b.canWalk("Mariatorget", "Kungsträdgården", 25)
    b.canWalk("Mariatorget", "Slottet", 21)

    # Gå från Zinkensdamm till VART DU VILL...
    b.canWalk("Zinkensdamm", "Odengatan", 42)
    b.canWalk("Zinkensdamm", "Vasaparken", 39)
    b.canWalk("Zinkensdamm", "Norrtull", 44)
    b.canWalk("Zinkensdamm", "Eriksbergsgatan", 28)
    b.canWalk("Zinkensdamm", "Kungsträdgården", 30)
    b.canWalk("Zinkensdamm", "Slottet", 25)
  
    # Gå från Odengatan till VART DU VILL...
    b.canWalk("Odengatan", "Vasaparken", 19)
    b.canWalk("Odengatan", "Norrtull", 16)
    b.canWalk("Odengatan", "Eriksbergsgatan", 17)
    b.canWalk("Odengatan", "Kungsträdgården", 31)
    b.canWalk("Odengatan", "Slottet", 36)

    # Gå från Vasaparken till VART DU VILL...
    b.canWalk("Vasaparken", "Norrtull", 16)
    b.canWalk("Vasaparken", "Eriksbergsgatan", 24)
    b.canWalk("Vasaparken", "Kungsträdgården", 31)
    b.canWalk("Vasaparken", "Slottet", 33)

    # Gå från Norrtull till VART DU VILL...
    b.canWalk("Norrtull", "Eriksbergsgatan", 17)
    b.canWalk("Norrtull", "Kungsträdgården", 31)
    b.canWalk("Norrtull", "Slottet", 36)

    # Gå från Eriksbergsgatan till VART DU VILL...
    b.canWalk("Eriksbergsgatan", "Kungsträdgården", 23)
    b.canWalk("Eriksbergsgatan", "Slottet", 30)

    # Gå från Kungsträdgården till VART DU VILL...
    b.canWalk("Kungsträdgården", "Slottet", 16)



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

