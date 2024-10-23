#  Task is to take a graph of cities connected by roads 
#  and either add or destroy roads so that there is exactly one path between every pair of distinct cities.
#  This could be a case of turning the graphs into a minimum spanning tree, which will connect all the cities at a minimum cost

#  Implement Union find
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent != x:
            self.parent = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rX = self.find(x)
        rY = self.find(y)

        if rX != rY:
            if self.rank[rX] > rY:
                self.parent[rY] = rX
            elif self.rank[rX] < rY:
                self.parent[rX] = rY
            else:
                self.parent[rX] = rY
                self.rank[rX] += 1
            return True
        return False
    

def solution(n, country, build, destroy):
    edges = []

    # collect edges based on country and build or destroy costs
    for i in range(n):
        for j in range(i + 1, n):
            if country[i][j] == '1':
                dcost = costConvert(destroy[i][j])
                edges.append((dcost, i, j, "destroy"))
            else:
                bcost = costConvert(build[i][j])
                edges.append((bcost, i, j, "build"))

    # sort edges by cost
    edges.sort()

    # use union find (aka kruskals algorithm) to find the minimum spanning tree
    unionf = UnionFind(n)
    totalCost =  0

    for cost, u, v, action in edges:
        if unionf.union(u, v):
            if action == "build":
                totalCost += cost
            # destroyed edges should be counted as negative cost
            elif action == "destroy":
                totalCost += cost

    return totalCost

# helper function to convert letters to cost
def costConvert(c):
    if 'A' <= c <= 'Z':
        return ord(c) - ord('A')
    elif 'a' <= c <= 'z':
        return ord(c) - ord('a') + 26
    return 0


def parseInput():
    # Will be replaced with actual inputs
    countryInput = "000,000,000"
    buildInput = "ABD,BAC,DCA"
    destroyInput = "ABD,BAC,DCA"


if __name__ == "__main__":
    print()