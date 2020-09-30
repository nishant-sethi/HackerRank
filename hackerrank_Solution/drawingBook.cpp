#include <vector>
#include <iostream>
#include <algorithm>

static int total_pages(const int& n) {
    return (n + 2) / 2;
}

int main() {
    
    int n,p;
    std::cin >> n >> p;
    
    int entire_book = total_pages(n);
    
    int from_front = total_pages(p) - 1;
    int from_back = entire_book - from_front - 1;
    
    std::cout << std::min(from_front, from_back) << '\n';
    
    return 0;
}
