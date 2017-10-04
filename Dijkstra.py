import traveller
import map

# Implements Dijkstra's algorithm
def dijkstra(traveller, nodes):

    # Assigns initial values
    curr_trav = traveller
    curr_node = traveller.currentNode
    curr_dist = 0
    visited = {}
    unvisited = {}
    for node in nodes:
        unvisited[nodes[node]] = {"dist": float("inf"), "move": None}  # Saves distance to the node and the move used
    unvisited[curr_node]["dist"] = curr_dist  # Start node takes 0 time to travel to

    # Iterates until we have reached the goal
    while not curr_trav.isAtGoal():
        moves = curr_trav.findLegalMoves()  # Generates all moves

        # Updates values for each unvisited node and saves the move used to get there
        for move in moves:
            alt_dist = move[2] + unvisited[curr_node]["dist"]  # Distance for next travel + distance for previous travels
            end_node = move[0]  # Node we travel to with this move
            if end_node in unvisited:  # Needs to be a node we haven't already explored
                if alt_dist < unvisited[end_node]["dist"]:  # Checks if the move is better than previous moves
                    unvisited[end_node] = {"dist": alt_dist, "move": move}

        # Saves the node in visited and removes it from unvisited
        visited[curr_node] = unvisited
        del unvisited[curr_node]

        # Selects the node with the minimum dist that hasn't been visited yet
        min_dist = float("inf")
        next_node = None
        for node in unvisited:
            if unvisited[node]["dist"] < min_dist:
                min_dist = unvisited[node]["dist"]
                next_node = node
        curr_node = next_node

        # Updates traveler to move to the next node
        curr_trav = curr_trav.moveTo(unvisited[next_node]["move"])

    #print(visited)
    return curr_trav  # Contains the historic moves

def main():

    with open("./data/test/register.json", encoding="UTF-8") as f:
        nameTable = eval(f.read())

    start = nameTable["Slussen"]
    goal = nameTable["Tekniska högskolan"]

    m = map.Map("./data/test/walk.mat", "./data/test/subway.mat", "./data/test/bus.mat")
    t = traveller.Traveller(m, start)
    t.setTarget(goal)

    path_result = dijkstra(t, nameTable)
    print("Path found:")
    print(path_result)

if __name__ == "__main__":
    main()


'''
Ge startnoden värdet 0 och resterande inf
Sätt startnoden som current och spara övriga noder i unvisited
    För nuvarande noden, beräkna avståndet till alla grannar. Om nytt kortaste, spara detta
    Ta bort nuvarande noden från unvisited och lägg till den i visited
    Om destinationsnoden är markerad visisted, avbryt
    Välj unvisited noden med minst avstånd, sätt den som current och repeat

'''