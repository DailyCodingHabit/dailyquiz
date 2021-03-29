
#include <iostream>
#include <typeinfo>

int daily = 1;

int main() {
  int& coding = daily, daily; 
  daily = 2;
  std::cout<< (&typeid(daily) == &typeid(coding));
  std::cout << coding << daily;
}


