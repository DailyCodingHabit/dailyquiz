


#include <iostream>
float dailyCodingHabit (float x){
    int n = x + 2 / 2;
    x = x* n - 0.5f * x;
    return x;
}

int main() {
    std::cout << dailyCodingHabit(2);
    return 0;
}

// 5