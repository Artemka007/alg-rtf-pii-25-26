#include <string>
#include <cmath>
#include <vector>
/**
        self.s = s
        self.n = len(s)
        self.base = base
        self.mod = mod
        
        max_len = self.n + 5
        self.pows = [1] * (max_len)
        self.hashes = [0] * (self.n + 1)
        
        for i in range(1, max_len):
            self.pows[i] = (self.pows[i-1] * base) % mod
        
        for i in range(self.n):
            self.hashes[i+1] = (self.hashes[i] * base + ord(s[i])) % mod */
long hash_str(int n, std::string s) {
    long mod = pow(10, 9) + 7;
    long base = 311;

    std::vector<int> pows(n + 5);
    std::vector<int> hashes(n + 1);
    
    for (long i = 1; i < n + 5; i++) {
        pows[i] = (pows[i - 1] * base) % mod;
    }
    
    for (long i = 0; i < n; i++) {
        hashes[i] = (hashes[i - 1] * base + std::string::) % mod;
    }
}


int main() {
    int n, m;
    std::string s, t;

    for (int pref_l = 1; pref_l < n; pref_l++) {
        for (int postf_l = 1; postf_l < n - pref_l - 1; postf_l++) {
            
        }   
    }

    return 0;
}