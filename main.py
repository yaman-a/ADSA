# union find class implementation
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # compress paths
        return self.parent[x]
    
    def union(self, x, y):
        rX = self.find(x)
        rY = self.find(y)

        if rX != rY:
            # union by rank
            if self.rank[rX] > self.rank[rY]:
                self.parent[rY] = rX
            elif self.rank[rX] < self.rank[rY]:
                self.parent[rX] = rY
            else:
                self.parent[rY] = rX
                self.rank[rX] += 1
            return True  # if union was successful
        return False  # if x and y were already connected

def solution(n, country, build, destroy):
    # create arrays for destroy and build costs
    toRemove = []  # existing roads that might need to be removed
    toCreate = []  # missing roads that might be built

    # collect edges from the input country, build, and destroy matrices
    for i in range(n):
        for j in range(i + 1, n):
            if country[i][j] == '1':  # road exists, check destroy cost
                dcost = costConvert(destroy[i][j])
                toRemove.append((dcost, i, j)) 
            else:  # road does not exist, check build cost
                bcost = costConvert(build[i][j])
                toCreate.append((bcost, i, j)) 

    # sort toRemove in descending order
    toRemove.sort(reverse=True, key=lambda x: x[0])

    # sort toCreate in ascending order
    toCreate.sort(key=lambda x: x[0])

    # initialize union find for all cities
    unionFind = UnionFind(n)
    totalCost = 0

    # process the roads that already exist 
    for dcost, u, v in toRemove:
        if not unionFind.union(u, v):  # if they were already connected, it's a cycle
            totalCost += dcost 

    # process the roads that don't exist
    for bcost, u, v in toCreate:
        if unionFind.union(u, v):  # if they weren't connected, we connect them
            totalCost += bcost

    return totalCost

# helper function to convert letters to cost
def costConvert(c):
    if 'A' <= c <= 'Z':
        return ord(c) - ord('A')
    elif 'a' <= c <= 'z':
        return ord(c) - ord('a') + 26
    return 0

# parse input
def parseInput():
    inputLine = input().strip()
    countryInput, buildInput, destroyInput = inputLine.split(' ')

    country = [list(row) for row in countryInput.split(',')]
    build = [list(row) for row in buildInput.split(',')]
    destroy = [list(row) for row in destroyInput.split(',')]

    n = len(country)
    return n, country, build, destroy

# main
if __name__ == "__main__":
    n, country, build, destroy = parseInput()
    result = solution(n, country, build, destroy)
    print(result)