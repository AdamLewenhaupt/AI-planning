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

# Runs Dijkstra "iterations" times and chooses the route that was fastest the most times.
# Returns the most common path and its average time and variance, and how often the most common and second most common paths were chosen
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
        if len(paths[path]) > max_length:
            second_max_length = max_length
            second_most_common_path = most_common_path
            max_length = len(paths[path])
            most_common_path = path
        if max_length > len(paths[path]) > second_max_length:
            second_max_length = len(paths[path])
            second_most_common_path = path

    # Calculates its shortest, average, and longest time
    path_times = sorted(paths[most_common_path])
    mean = round(sum(path_times) / float(len(path_times)), 1)  # Average time of the path
    variance = np.var(path_times)
    percent_occ = round(float(len(path_times)) / float(iterations), 3)  # Percent of times the most common path was chosen
    try:  # Gives error if the same path was chosen every single iteration
        percent_occ_second = round(float(len(paths[second_most_common_path])) / float(iterations), 3)  # Percent of times the second most common path was chosen
    except:
        percent_occ_second = 0.00

    return path_results[most_common_path], mean, variance, percent_occ, percent_occ_second

# Used to calculate how many iterations are required
# Works by increasing the number of iterations and printing how often the most common paths are chosen
def get_req_iterations(start, goal, nameTable):
    for i in range(100, 1500, 100):
        paths = {}
        for j in range(0, 100):
            most_common_path, mean, variance, percent_occ, percent_occ_second = mean_dijkstra(start, goal, nameTable, i)
            path = str(most_common_path)
            if path in paths:
                paths[path] += 1
            else:
                paths[path] = 1

        print(i, end="\t")
        for path in paths:
            print(paths[path], end="\t")
        print()

def main():

    with open("./data/test/register.json", encoding="UTF-8") as f:
        nameTable = eval(f.read())

    # get_req_iterations(nameTable["Tekniska högskolan"], nameTable["Slussen"], nameTable)  # Only used once

    # Lists of start- and goal-points to be studied
    start_points = [nameTable["Tekniska högskolan"], nameTable["Norrtull"], nameTable["Tekniska högskolan"],
                    nameTable["Tekniska högskolan"], nameTable["S:t Eriksplan"], nameTable["S:t Eriksplan"],
                    nameTable["Kungsholmen"], nameTable["Eriksbergsgatan"], nameTable["Eriksbergsgatan"],
                    nameTable["Eriksbergsgatan"]]
    goal_points = [nameTable["Slussen"], nameTable["Slussen"], nameTable["Norrtull"],
                   nameTable["Mariatorget"], nameTable["Kungsträdgården"], nameTable["Mariatorget"],
                   nameTable["Zinkensdamm"], nameTable["Slussen"], nameTable["Odengatan"],
                   nameTable["Kungsholmen"]]
    iterations = 1000  # Number of iterations Dijkstra's algorithm is run

    # Computes Dijkstra's algorithm for each pair of start- and goal-points
    for i in range(len(start_points)):

        # Computes Dijkstra and measures the elapsed time
        start_time = time.time()
        most_common_path, mean, variance, percent_occ, percent_occ_second = mean_dijkstra(start_points[i], goal_points[i], nameTable, iterations)
        time_elapsed = time.time() - start_time

        # Prints the result in a table format
        start = str(most_common_path).split(" -> ")[0]  # Fetches the start and goal-points for the print
        goal = str(most_common_path).split(" -> ")[-1]
        print(start, "\t", goal, "\t", mean, "\t", variance, "\t", percent_occ, "\t", percent_occ_second, "\t", time_elapsed, "\t", most_common_path)

if __name__ == "__main__":
    main()