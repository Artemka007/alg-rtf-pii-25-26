#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

int main() {
    int N;
    std::cin >> N;

    std::vector<int> graph[101];
    int team[101] = {0};
    bool visited[101] = {false};

    for (int i = 1; i <= N; i++) {
        int j;
        std::cin >> j;
        while (j != 0) {
            graph[i].push_back(j);
            std::cin >> j;
        }
    }

    std::vector<std::pair<int, int>> degrees;
    for (int i = 1; i <= N; i++) {
        degrees.push_back({graph[i].size(), i});
    }
    std::sort(degrees.rbegin(), degrees.rend());

    for (auto& t : degrees) {
        int start = t.second;
        if (!visited[start]) {
            std::queue<int> q;
            q.push(start);
            team[start] = 1;
            visited[start] = true;

            while (!q.empty()) {
                int current = q.front();
                q.pop();

                int count_team1 = 0, count_team2 = 0;
                for (int neighbor : graph[current]) {
                    if (team[neighbor] == 1) count_team1++;
                    if (team[neighbor] == 2) count_team2++;
                }

                if (team[current] == 1 && count_team2 == 0) {
                    team[current] = 2;
                } else if (team[current] == 2 && count_team1 == 0) {
                    team[current] = 1;
                }

                for (int neighbor : graph[current]) {
                    if (!visited[neighbor]) {
                        int neighbor_team1 = 0, neighbor_team2 = 0;
                        for (int neighbor_of_neighbor : graph[neighbor]) {
                            if (team[neighbor_of_neighbor] == 1) neighbor_team1++;
                            if (team[neighbor_of_neighbor] == 2) neighbor_team2++;
                        }
                        
                        team[neighbor] = (neighbor_team1 > neighbor_team2) ? 2 : 1;
                        visited[neighbor] = true;
                        q.push(neighbor);
                    }
                }
            }
        }
    }

    bool valid = true;
    for (int i = 1; i <= N; i++) {
        bool has_other_team = false;
        for (int friend_ : graph[i]) {
            if (team[friend_] != team[i]) {
                has_other_team = true;
                break;
            }
        }
        if (!has_other_team) {
            valid = false;
            break;
        }
    }

    if (valid) {
        std::vector<int> team1;
        for (int i = 1; i <= N; i++) {
            if (team[i] == 1) team1.push_back(i);
        }
        
        std::cout << team1.size() << std::endl;
        for (size_t i = 0; i < team1.size(); i++) {
            std::cout << team1[i];
            if (i < team1.size() - 1) std::cout << " ";
        }
        std::cout << std::endl;
    } else {
        std::cout << 0 << std::endl;
    }

    return 0;
}