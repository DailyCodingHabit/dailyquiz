



#include <iostream>
using namespace std;
int main() {
    int daily,coding,habit = 3;
    for (daily=1; daily <= habit; ++daily) {
      for (coding=1; coding <= daily; ++coding) {
            if (min(daily,coding) % 2) {
                cout<<"*";
            }
        }
    }
    return 0;
}


