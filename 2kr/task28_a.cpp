#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

// Р¤СѓРЅРєС†РёСЏ РґР»СЏ РїРѕСЃС‚СЂРѕРµРЅРёСЏ СЃСѓС„С„РёРєСЃРЅРѕРіРѕ РјР°СЃСЃРёРІР°
vector<int> suffix_array(vector<int> &s) {
    s.push_back(0);  // РґРѕР±Р°РІР»СЏРµРј РЅСѓР»РµРІРѕР№ СЃРёРјРІРѕР» РІ РєРѕРЅРµС† СЃС‚СЂРѕРєРё
    int n = (int) s.size();
    int cnt = 0;
    int cls = 0;
    vector<int> c(n), p(n);
    
    map<int, vector<int>> t;
    for (int i = 0; i < n; i++)
        t[s[i]].push_back(i);
    
    // В«РЅСѓР»РµРІРѕР№В» СЌС‚Р°Рї
    for (auto &x : t) {
        for (int u : x.second)
            c[u] = cls, p[cnt++] = u;
        cls++;
    }
    
    // РїРѕРєР° РІСЃРµ СЃСѓС„С„РёРєСЃС‹ РЅРµ СЃС‚Р°Р»Рё СѓРЅРёРєР°Р»СЊРЅС‹РјРё
    for (int l = 1; cls < n; l++) {
        vector<vector<int>> a(cls);
        vector<int> _c(n);
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
    
    // РЈР±РёСЂР°РµРј РґРѕР±Р°РІР»РµРЅРЅС‹Р№ РЅСѓР»РµРІРѕР№ СЃРёРјРІРѕР» РёР· РёСЃС…РѕРґРЅРѕР№ СЃС‚СЂРѕРєРё
    s.pop_back();
    
    return vector<int>(p.begin() + 1, p.end());
}

// Р¤СѓРЅРєС†РёСЏ РґР»СЏ РІС‹С‡РёСЃР»РµРЅРёСЏ LCP РјР°СЃСЃРёРІР°
vector<int> calc_lcp(const vector<int> &val, const vector<int> &sa) {
    int n = val.size();
    vector<int> rank(n);
    vector<int> lcp(n - 1); // LCP РјРµР¶РґСѓ n СЃСѓС„С„РёРєСЃР°РјРё = n-1 Р·РЅР°С‡РµРЅРёР№
    
    // РЎС‚СЂРѕРёРј РјР°СЃСЃРёРІ rank (РѕР±СЂР°С‚РЅС‹Р№ Рє sa)
    for (int i = 0; i < n; i++) {
        rank[sa[i]] = i;
    }
    
    int h = 0;
    for (int i = 0; i < n; i++) {
        if (rank[i] > 0) {
            int j = sa[rank[i] - 1];
            // РќР°С…РѕРґРёРј LCP РјРµР¶РґСѓ СЃСѓС„С„РёРєСЃР°РјРё, РЅР°С‡РёРЅР°СЋС‰РёРјРёСЃСЏ РІ i Рё j
            while (i + h < n && j + h < n && val[i + h] == val[j + h]) {
                h++;
            }
            lcp[rank[i] - 1] = h;
            if (h > 0) h--;
        }
    }
    
    return lcp;
}

// РћСЃРЅРѕРІРЅР°СЏ С„СѓРЅРєС†РёСЏ РґР»СЏ РїРѕРґСЃС‡РµС‚Р° СЂР°Р·Р»РёС‡РЅС‹С… РїРѕРґСЃС‚СЂРѕРє
long long count_distinct_substrings(const string &str) {
    if (str.empty()) return 0;
    
    int n = str.size();
    
    // РџСЂРµРѕР±СЂР°Р·СѓРµРј СЃС‚СЂРѕРєСѓ РІ РІРµРєС‚РѕСЂ С‡РёСЃРµР» (РѕС‚ 1 РґРѕ 26)
    vector<int> s(n);
    for (int i = 0; i < n; i++) {
        s[i] = str[i] - 'a' + 1;
    }
    
    // РЎС‚СЂРѕРёРј СЃСѓС„С„РёРєСЃРЅС‹Р№ РјР°СЃСЃРёРІ
    vector<int> sa = suffix_array(s);
    
    // РџСЂРѕРІРµСЂСЏРµРј СЂР°Р·РјРµСЂ СЃСѓС„С„РёРєСЃРЅРѕРіРѕ РјР°СЃСЃРёРІР°
    if (sa.size() != n) {
        cerr << "Error: Suffix array size mismatch. Expected: " << n 
             << ", Got: " << sa.size() << endl;
        return -1;
    }
    
    // Р’С‹С‡РёСЃР»СЏРµРј LCP
    vector<int> lcp = calc_lcp(s, sa);
    
    // РџРѕРґСЃС‡РёС‚С‹РІР°РµРј РѕР±С‰РµРµ РєРѕР»РёС‡РµСЃС‚РІРѕ РїРѕРґСЃС‚СЂРѕРє
    long long total_substrings = (long long)n * (n + 1) / 2;
    
    // Р’С‹С‡РёС‚Р°РµРј РїРѕРІС‚РѕСЂСЏСЋС‰РёРµСЃСЏ РїРѕРґСЃС‚СЂРѕРєРё (СЃСѓРјРјР° LCP)
    long long repeated_substrings = 0;
    for (int i = 0; i < n - 1; i++) {
        repeated_substrings += lcp[i];
    }
    
    return total_substrings - repeated_substrings;
}

int main() {
    string s;
    cin >> s;
    cout << count_distinct_substrings(s) << endl;
    return 0;
}