#include <stdlib.h>

int main()
{
    int *a = malloc(sizeof(int));
    int tmp = 0;

    for (int i = 0; i < 10; i++) {
        a[0] += i;
    }
    tmp = *a;
    free(a);
    return tmp;
}
