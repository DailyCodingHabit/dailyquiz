

#include <iostream>
using namespace std;
int main()
{
    int count = 1;
    for ( int i = 10; i > 9; i--) {
        count = 5 - i + 12 / 2 * 4;
    }
    std::cout << count << std::endl;
    return 0;
}

