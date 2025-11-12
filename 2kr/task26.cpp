#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

std::vector<int> manacher_odd(int n, std::string s) {
    std::vector<int> d(n, 1);
    int l = 0, r = 0;

    for (int i = 1; i < n; i++) {
        if (i < r) {
            d[i] = std::min(r - i + 1, d[l + r - i]);
        }
        while (i - d[i] >= 0 && i + d[i] < n && s[i - d[i]] == s[i + d[i]]) {
            d[i]++;
        }
        if (i + d[i] - 1 > r) {
            l = i - d[i] + 1, r = i + d[i] - 1;
        }
    }

    return d;
}

std::vector<int> manacher_even(int n, std::string s) {
    std::vector<int> d(n, 0);
    int l = -1, r = -1;

    for (int i = 0; i < n - 1; i++) {
        if (i < r) {
            d[i] = std::min(r - i, d[l + r - i - 1]);
        }
        while (i - d[i] >= 0 && i + d[i] + 1 < n && s[i - d[i]] == s[i + d[i] + 1]) {
            d[i]++;
        }
        if (i + d[i] > r) {
            l = i - d[i] + 1, r = i + d[i];
        }
    }

    return d;
}

int main() {
    std::string s;
    std::cin >> s;

    int n = s.length();
    if (n == 0) {
        std::cout << "" << std::endl;
        return 0;
    }

    if (n == 1) {
        std::cout << s + s << std::endl;
        return 0;
    }

    std::vector<int> odd_d = manacher_odd(n, s);
    std::vector<int> even_d = manacher_even(n, s);

    int longest_suffix_start = n;
    
    for (int i = 0; i < n; i++) {
        int radius = odd_d[i];
        int start = i - radius + 1;
        int end = i + radius - 1;
        
        if (end == n - 1 && start > 0) {
            longest_suffix_start = std::min(longest_suffix_start, start);
        }
    }
    
    for (int i = 0; i < n; i++) {
        int radius = even_d[i];
        if (radius > 0) {
            int start = i - radius + 1;
            int end = i + radius;
            
            if (end == n - 1 && start > 0) {
                longest_suffix_start = std::min(longest_suffix_start, start);
            }
        }
    }

    std::string result = s;
    
    if (longest_suffix_start < n) {
        for (int i = longest_suffix_start - 1; i >= 0; i--) {
            result += s[i];
        }
    } else {
        for (int i = n - 1; i >= 1; i--) {
            result += s[i];
        }
    }

    std::cout << result << std::endl;
    return 0;
}