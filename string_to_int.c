#include <math.h>
#include <stdio.h>


int stringToInt(char * str, int str_len) {
    int x = 0;
    for (int i = 0; i < str_len; i++) {
        x += (str[i] - '0') * pow(10, str_len - i - 1);
    }
    return x;
}

int main() {
    char str[] = {'3', '7', '1'};
    printf("%d\n", stringToInt(str, 3));
    return 0;
}
