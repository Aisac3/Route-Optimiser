import numpy as np

matrix = np.array([
    [0, 7032.90, 6843.53, 3888.74, 6107.54],
    [7032.90, 0, 6492.82, 9111.22, 8931.39],
    [6843.53, 6492.82, 0, 10416.69, 4505.01],
    [3888.74, 9111.22, 10416.69, 0, 10004.59],
    [6107.54, 8931.39, 4505.01, 10004.59, 0]
])

def nearest_neighbor_tsp(matrix):
    n = len(matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    total_distance = 0

    for _ in range(n - 1):
        last = route[-1]
        nearest = None
        min_dist = float('inf')

        for i in range(n):
            if not visited[i] and matrix[last][i] < min_dist:
                min_dist = matrix[last][i]
                nearest = i

        route.append(nearest)
        visited[nearest] = True
        total_distance += min_dist

    # Return to start
    total_distance += matrix[route[-1]][0]
    route.append(0)

    return route, total_distance

if __name__ == "__main__":
    route, distance = nearest_neighbor_tsp(matrix)

    print("Optimized Route:", route)
    print("Total Distance (meters):", distance)