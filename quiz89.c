


#include <stdio.h>
#include <string.h>
int main() {
    char str1[100] = "*", str2[] = "*";
    strcat(str1, str2);
    size_t i = 0;
    for (; i < strlen(str2)*strlen(str1); i++) {
        puts(str2);
    }
    return 0;
}



// **