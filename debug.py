class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            return True
        return False

def solution(n, country, build, destroy):
    edges = []

    # Collect edges based on existing roads and their build/destroy costs
    for i in range(n):
        for j in range(i + 1, n):
            if country[i][j] == '1':  # Road exists
                dcost = costConvert(destroy[i][j])
                edges.append((dcost, i, j, "destroy"))  # Edge with destroy cost
            else:  # No road exists
                bcost = costConvert(build[i][j])
                edges.append((bcost, i, j, "build"))  # Edge with build cost

    # Sort edges by cost (Kruskal's algorithm)
    edges.sort()

    # Use Union-Find to find the minimum spanning tree
    union_find = UnionFind(n)
    totalCost = 0
    roadsBuilt = 0

    for cost, u, v, action in edges:
        if union_find.union(u, v):
            # Add cost for building or destroying
            totalCost += cost
            roadsBuilt += 1
        # Stop once we have n-1 edges (the minimum spanning tree)
        if roadsBuilt == n - 1:
            break

    return totalCost

def costConvert(c):
    # Convert letter cost to numerical value: A-Z -> 0-25, a-z -> 26-51
    if 'A' <= c <= 'Z':
        return ord(c) - ord('A')
    elif 'a' <= c <= 'z':
        return ord(c) - ord('a') + 26
    return 0

def parseInput():
    inputLine = input().strip()
    countryInput, buildInput, destroyInput = inputLine.split(' ')

    # Convert input strings into 2D arrays for country, build, destroy
    country = [list(row) for row in countryInput.split(',')]
    build = [list(row) for row in buildInput.split(',')]
    destroy = [list(row) for row in destroyInput.split(',')]

    n = len(country)  # Number of cities
    return n, country, build, destroy

if __name__ == "__main__":
    n, country, build, destroy = parseInput()
    result = solution(n, country, build, destroy)
    print(result)
