#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int n;
    std::cin >> n;
    
    std::vector<std::pair<int, int>> lectures(n);
    
    for (int i = 0; i < n; i++) {
        std::cin >> lectures[i].first >> lectures[i].second;
    }
    
    sort(lectures.begin(), lectures.end(), [](const std::pair<int, int>& a, const std::pair<int, int>& b) {
        return a.second < b.second;
    });
    
    int count = 0;
    int last_end = -1;
    
    for (const auto& lecture : lectures) {
        int start = lecture.first;
        int end = lecture.second;
        
        if (start > last_end) {
            count++;
            last_end = end;
        }
    }
    
    std::cout << count << std::endl;
    
    return 0;
}