#include <cmath>
#include <iostream>
#include <unordered_map>
#include <vector>

bool is_prime(int n) {
    if (n < 2) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;
    
    int limit = static_cast<int>(std::sqrt(n));
    for (int i = 3; i <= limit; i += 2) {
        if (n % i == 0) return false;
    }
    return true;
}

int main() {
    int MOD = 10e9+9;
    int n;
    std::cin >> n;

    std::vector<int> primes;
    for (int i = 100; i < 1000; i++) {
        if (is_prime(i)) {
            primes.push_back(i);
        }
    }

    std::unordered_map<int, std::vector<int>> transitions;
    for (int prime : primes) {
        int prefix = prime / 10;
        int suffix = prime % 100;
        transitions[prefix].push_back(suffix);
    }

    std::unordered_map<int, long long> dp;
    for (int prime : primes) {
        int suffix = prime % 100;
        dp[suffix]++;
    }

    for (int l = 4; l <= n; l++) {
        std::unordered_map<int, long long> new_dp;
        
        for (const auto& [state, count] : dp) {
            if (transitions.find(state) != transitions.end()) {
                for (int next_state : transitions[state]) {
                    new_dp[next_state] = (new_dp[next_state] + count) % MOD;
                }
            }
        }
        
        dp = new_dp;
    }

    long long result = 0;
    for (const auto& [state, count] : dp) {
        result = (result + count) % MOD;
    }

    std::cout << result << std::endl;

    return 0;
}