#include <iostream>
#include <vector>
#include <climits>

int main() {
    int n, k;
    std::cin >> n >> k;
    
    std::vector<int> plants(k);
    for (int i = 0; i < k; i++) {
        std::cin >> plants[i];
        plants[i]--;
    }
    
    std::vector<std::vector<int>> cost(n, std::vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            std::cin >> cost[i][j];
        }
    }
    
    std::vector<bool> inMST(n, false);
    std::vector<int> minEdge(n, INT_MAX);
    
    for (int p : plants) {
        inMST[p] = true;
        minEdge[p] = 0;
    }
    
    for (int p : plants) {
        for (int v = 0; v < n; v++) {
            if (!inMST[v] && cost[p][v] < minEdge[v]) {
                minEdge[v] = cost[p][v];
            }
        }
    }
    
    int totalCost = 0;
    
    for (int i = k; i < n; i++) {
        int minCost = INT_MAX;
        int nextCity = -1;
        
        for (int v = 0; v < n; v++) {
            if (!inMST[v] && minEdge[v] < minCost) {
                minCost = minEdge[v];
                nextCity = v;
            }
        }
        
        if (nextCity == -1) break;
        
        inMST[nextCity] = true;
        totalCost += minCost;
        
        for (int v = 0; v < n; v++) {
            if (!inMST[v] && cost[nextCity][v] < minEdge[v]) {
                minEdge[v] = cost[nextCity][v];
            }
        }
    }
    
    std::cout << totalCost << std::endl;
    
    return 0;
}