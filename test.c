#include <stdio.h>

int print_something(int a)
{
    printf("%d ", a);
}

int main(void)
{
    int a = 0;

    for (int i = 0; i < 10; i++) {
        a += i;
        print_something(a);
    }
    return a;
}
