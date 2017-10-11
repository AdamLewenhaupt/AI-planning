import traveller
import map
import numpy as np
import time

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

    traveller_history = []
    counter = 0

    # Iterates until we have reached the goal
    while not curr_trav.isAtGoal():
        moves = curr_trav.findLegalMoves()  # Generates all moves

        # Updates values for each unvisited node and saves the move used to get there
        for move in moves:
            alt_dist = move[2] + unvisited[curr_node]["dist"]  # Distance for next travel + distance for previous travels
            end_node = move[0]  # Node we travel to with this move
            if end_node in unvisited:  # Needs to be a node we haven't already explored
                if alt_dist < unvisited[end_node]["dist"]:  # Checks if the move is better than previous moves
                    unvisited[end_node] = {"dist": alt_dist, "move": move, "counter": counter}  # Counter is the index of the state

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
        traveller_history.append(curr_trav)  # Saves the current state
        curr_trav = traveller_history[unvisited[next_node]["counter"]].moveTo(unvisited[next_node]["move"])  # Makes the move for the appropriate state

        counter += 1

    return curr_trav  # Contains the historic moves

# Runs Dijkstra 100 times and takes the route that was fastest the most times.
# Returns the most common path, its shortest, average, and longest time (for the times it was chosen as the fastest)
def mean_dijkstra(start, goal, nodes, iterations):

    # Iterates X times and saves the results in a dict
    paths = {}  # Key is the printed representation of the route, also contains a list of all its recorded times
    path_results = {}
    for i in range(0, iterations):
        m = map.Map("./data/test/walk.mat", "./data/test/subway.mat", "./data/test/bus.mat")
        t = traveller.Traveller(m, start)
        t.setTarget(goal)
        path_result = dijkstra(t, nodes)
        if str(path_result.history) in paths:
            paths[str(path_result.history)].append(path_result.timeElapsed)
        else:
            paths[str(path_result.history)] = [path_result.timeElapsed]
            path_results[str(path_result.history)] = path_result

    # Chooses the most common path
    max_length = 0
    second_max_length = 0
    most_common_path = ""
    second_most_common_path = ""
    for path in paths:  # Keeps track of both the most common and the most common path
        #print(path_results[path])
        if len(paths[path]) > max_length:
            second_max_length = max_length
            second_most_common_path = most_common_path
            max_length = len(paths[path])
            most_common_path = path
        if max_length > len(paths[path]) > second_max_length:
            second_max_length = len(paths[path])
            second_most_common_path = path
        #print(path_results[path], len(paths[path]))

    # Calculates its shortest, average, and longest time
    path_times = sorted(paths[most_common_path])
    mean = round(sum(path_times) / float(len(path_times)), 1)  # Average time of the path
    variance = np.var(path_times)
    percent_occ = round(float(len(path_times)) / float(iterations), 3)  # Percent of times the most common path was chosen
    try:  # Gives error if the same path was chosen every single iteration
        percent_occ_second = round(float(len(paths[second_most_common_path])) / float(iterations), 3)  # Percent of times the second most common path was chosen
    except:
        percent_occ_second = 0.00
    #shortest = round(path_times[0], 1)
    #longest = round(path_times[len(path_times)-1], 1)

    #return path_results[most_common_path], shortest, mean, longest
    return path_results[most_common_path], mean, variance, percent_occ, percent_occ_second

def main():

    with open("./data/test/register.json", encoding="UTF-8") as f:
        nameTable = eval(f.read())
    #print(nameTable)
    start_points = [nameTable["Tekniska högskolan"], nameTable["Norrtull"], nameTable["Tekniska högskolan"],
                    nameTable["Tekniska högskolan"], nameTable["S:t Eriksplan"], nameTable["S:t Eriksplan"],
                    nameTable["Kungsholmen"], nameTable["Eriksbergsgatan"], nameTable["Eriksbergsgatan"],
                    nameTable["Eriksbergsgatan"]]
    goal_points = [nameTable["Slussen"], nameTable["Slussen"], nameTable["Norrtull"],
                   nameTable["Mariatorget"], nameTable["Kungsträdgården"], nameTable["Mariatorget"],
                   nameTable["Zinkensdamm"], nameTable["Slussen"], nameTable["Odengatan"],
                   nameTable["Kungsholmen"]]
    iterations = 1000
    #start = nameTable["Eriksbergsgatan"]
    #goal = nameTable["Kungsholmen"]

    for i in range(len(start_points)):

        #most_common_path, shortest, mean, longest = mean_dijkstra(start_points[i], goal_points[i], nameTable)
        #print("Most common path: ", most_common_path, "\nShortest:\t", shortest, "\nMean:\t\t", mean, "\nLongest:\t", longest)

        start_time = time.time()
        most_common_path, mean, variance, percent_occ, percent_occ_second = mean_dijkstra(start_points[i], goal_points[i], nameTable, iterations)
        time_elapsed = time.time() - start_time  # Time it took to compute Dijkstra's

        #print("Most common path: ", most_common_path, "\nMean:\t\t", mean, "\nVariance:\t",variance)
        start = str(most_common_path).split(" -> ")[0]  # Fetches the start and end points for the print
        goal = str(most_common_path).split(" -> ")[-1]
        print(start, "\t", goal, "\t", mean, "\t", variance, "\t", percent_occ, "\t", percent_occ_second, "\t", time_elapsed, "\t", most_common_path)  # Gives the output in a table format

    '''
    m = map.Map("./data/test/walk.mat", "./data/test/subway.mat", "./data/test/bus.mat")
    t = traveller.Traveller(m, start)
    t.setTarget(goal)

    path_result = dijkstra(t, nameTable)
    print("Path found:")
    print(path_result)
    print("Expected time: %d min." % path_result.timeElapsed)
    '''

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
