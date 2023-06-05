#include <stdlib.h>

int main()
{
    int *a = malloc(sizeof(int));
    int tmp = 0;

    tmp = *a;
    free(a);
    return tmp;
}
