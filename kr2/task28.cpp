#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>

std::vector<int> suffix_array(std::vector<int> &s) {
    s.push_back(0); 
    int n = (int) s.size();
    int cnt = 0;
    int cls = 0;
    std::vector<int> c(n), p(n);
    
    std::map<int, std::vector<int>> t;
    for (int i = 0; i < n; i++)
        t[s[i]].push_back(i);
    
    for (auto &x : t) {
        for (int u : x.second)
            c[u] = cls, p[cnt++] = u;
        cls++;
    }
    
    for (int l = 1; cls < n; l++) {
        std::vector<std::vector<int>> a(cls);
        std::vector<int> _c(n);
        int d = (1 << l) / 2;
        int _cls = cnt = 0;
        
        for (int i = 0; i < n; i++) {
            int k = (p[i] - d + n) % n;
            a[c[k]].push_back(k);
        }
        
        for (int i = 0; i < cls; i++) {
            for (size_t j = 0; j < a[i].size(); j++) {
                if (j == 0 || c[(a[i][j] + d) % n] != c[(a[i][j - 1] + d) % n])
                    _cls++;
                _c[a[i][j]] = _cls - 1;
                p[cnt++] = a[i][j];
            }
        }
        
        c = _c;
        cls = _cls;
    }
    
    s.pop_back();
    
    return std::vector<int>(p.begin() + 1, p.end());
}

// Функция для вычисления LCP массива
std::vector<int> calc_lcp(const std::vector<int> &val, const std::vector<int> &sa) {
    int n = val.size();
    std::vector<int> rank(n);
    std::vector<int> lcp(n - 1);
    
    for (int i = 0; i < n; i++) {
        rank[sa[i]] = i;
    }
    
    int h = 0;
    for (int i = 0; i < n; i++) {
        if (rank[i] > 0) {
            int j = sa[rank[i] - 1];
            while (i + h < n && j + h < n && val[i + h] == val[j + h]) {
                h++;
            }
            lcp[rank[i] - 1] = h;
            if (h > 0) h--;
        }
    }
    
    return lcp;
}

long long count_distinct_substrings(const std::string &str) {
    if (str.empty()) return 0;
    
    int n = str.size();
    
    std::vector<int> s(n);
    for (int i = 0; i < n; i++) {
        s[i] = str[i] - 'a' + 1;
    }
    
    std::vector<int> sa = suffix_array(s);
    
    if (sa.size() != n) {
        std::cerr << "Error: Suffix array size mismatch. Expected: " << n 
             << ", Got: " << sa.size() << std::endl;
        return -1;
    }
    
    std::vector<int> lcp = calc_lcp(s, sa);
    
    long long total_substrings = (long long)n * (n + 1) / 2;
    
    long long repeated_substrings = 0;
    for (int i = 0; i < n - 1; i++) {
        repeated_substrings += lcp[i];
    }
    
    return total_substrings - repeated_substrings;
}

int main() {
    std::string s;
    std::cin >> s;
    std::cout << count_distinct_substrings(s) << std::endl;
    return 0;
}