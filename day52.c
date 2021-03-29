

#include <stdio.h>
int main()
{
   int a=10; //variable declaration
   int *p;   //pointer variable declaration
   p=&a;     //store address of var a in pointer p
   printf("p:%x\n",p);  //accessing the address
   printf("p:%d\n",*p);   //accessing the value
   return 0;
}

// Output:
// p:31546914
// p:10



