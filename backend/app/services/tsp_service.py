import numpy as np


class TSPService:

    def build_distance_matrix(self, nodes, path_service):
        n = len(nodes)
        matrix = np.zeros((n, n))
        path_cache = {}

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                route = path_service.shortest_path(nodes[i], nodes[j])

                if route:
                    length = path_service.calculate_route_length(route)
                    matrix[i][j] = length
                    path_cache[(i, j)] = route
                else:
                    matrix[i][j] = float("inf")

        return matrix, path_cache

    def nearest_neighbor(self, matrix):
        n = len(matrix)
        visited = [False] * n
        route = [0]
        visited[0] = True

        for _ in range(n - 1):
            last = route[-1]
            next_city = int(np.argmin([
                matrix[last][j] if not visited[j] else float("inf")
                for j in range(n)
            ]))
            route.append(next_city)
            visited[next_city] = True

        return [int(x) for x in route]
    def calculate_total_distance(self, route, matrix):
        total = 0
        for i in range(len(route) - 1):
            total += matrix[route[i]][route[i+1]]
        return total


    def two_opt(self, route, matrix):
        best = route
        improved = True

        while improved:
            improved = False
            best_distance = self.calculate_total_distance(best, matrix)

            for i in range(1, len(best) - 2):
                for j in range(i + 1, len(best)):
                    if j - i == 1:
                        continue

                    new_route = best[:]
                    new_route[i:j] = best[j-1:i-1:-1]

                    new_distance = self.calculate_total_distance(new_route, matrix)

                    if new_distance < best_distance:
                        best = new_route
                        improved = True
                        break
                if improved:
                    break

        return [int(x) for x in best]

tsp_service = TSPService()