import numpy as np

def calculate_total_distance(route, matrix):
    total = 0
    for i in range(len(route) - 1):
        total += matrix[route[i]][route[i+1]]
    return total


def two_opt(route, matrix):
    best = route
    improved = True

    while improved:
        improved = False
        best_distance = calculate_total_distance(best, matrix)

        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route) - 1):
                if j - i == 1:
                    continue

                new_route = best[:]
                new_route[i:j] = best[j-1:i-1:-1]

                new_distance = calculate_total_distance(new_route, matrix)

                if new_distance < best_distance:
                    best = new_route
                    improved = True
                    break
            if improved:
                break

    return best

if __name__ == "__main__":
    matrix = np.array([
        [0, 7032.90, 6843.53, 3888.74, 6107.54],
        [7032.90, 0, 6492.82, 9111.22, 8931.39],
        [6843.53, 6492.82, 0, 10416.69, 4505.01],
        [3888.74, 9111.22, 10416.69, 0, 10004.59],
        [6107.54, 8931.39, 4505.01, 10004.59, 0]
    ])

    from tsp_nn import nearest_neighbor_tsp

    route, nn_distance = nearest_neighbor_tsp(matrix)

    print("Nearest Neighbor Route:", route)
    print("NN Distance:", nn_distance)

    improved_route = two_opt(route, matrix)
    improved_distance = calculate_total_distance(improved_route, matrix)

    print("\nAfter 2-Opt:")
    print("Improved Route:", improved_route)
    print("Improved Distance:", improved_distance)