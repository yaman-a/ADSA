#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Helper function to convert character cost to integer
int charToCost(char c) {
    if (c >= 'A' && c <= 'Z') return c - 'A';
    return c - 'a' + 26;
}

// Disjoint Set Union (Union-Find) to keep track of connected components
class DSU {
public:
    vector<int> parent, rank;
    
    DSU(int n) {
        parent.resize(n);
        rank.resize(n, 1);
        for (int i = 0; i < n; ++i) parent[i] = i;
    }

    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }

    bool unite(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
            return true;
        }
        return false;
    }
};

struct Edge {
    int u, v, cost;
    Edge(int u, int v, int cost) : u(u), v(v), cost(cost) {}
};

// Comparator for sorting edges based on cost
bool compareEdges(const Edge& a, const Edge& b) {
    return a.cost < b.cost;
}

int main() {
    string countryStr, buildStr, destroyStr;
    cin >> countryStr >> buildStr >> destroyStr;
    
    // Parsing the input
    vector<string> country, build, destroy;
    size_t pos = 0;
    while ((pos = countryStr.find(',')) != string::npos) {
        country.push_back(countryStr.substr(0, pos));
        countryStr.erase(0, pos + 1);
    }
    country.push_back(countryStr);
    
    pos = 0;
    while ((pos = buildStr.find(',')) != string::npos) {
        build.push_back(buildStr.substr(0, pos));
        buildStr.erase(0, pos + 1);
    }
    build.push_back(buildStr);
    
    pos = 0;
    while ((pos = destroyStr.find(',')) != string::npos) {
        destroy.push_back(destroyStr.substr(0, pos));
        destroyStr.erase(0, pos + 1);
    }
    destroy.push_back(destroyStr);
    
    int N = country.size();
    vector<Edge> edges;
    
    // Building the graph edges with their respective costs
    for (int i = 0; i < N; ++i) {
        for (int j = i + 1; j < N; ++j) {
            if (country[i][j] == '1') {
                // There's a road, consider destroying it
                edges.push_back(Edge(i, j, charToCost(destroy[i][j])));
            } else {
                // No road, consider building one
                edges.push_back(Edge(i, j, charToCost(build[i][j])));
            }
        }
    }
    
    // Sort edges by cost
    sort(edges.begin(), edges.end(), compareEdges);
    
    // Kruskal's algorithm to find MST
    DSU dsu(N);
    int totalCost = 0;
    
    for (const Edge& edge : edges) {
        if (dsu.unite(edge.u, edge.v)) {
            totalCost += edge.cost;
        }
    }
    
    cout << totalCost << endl;
    return 0;
}
