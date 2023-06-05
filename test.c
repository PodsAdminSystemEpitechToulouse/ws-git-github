#include <stdlib.h>
#include <stdio.h>

int main()
{
    int *a = malloc(sizeof(int));
    int tmp = 0;

    for (int i = 0; i < 10; i++) {
        a[0] += i;
        printf("%d\n", a[0]);
    }
    tmp = *a;
    free(a);
    return tmp;
}
