#include <stdio.h>
#include <stdlib.h>

int fibonacci(int n)
{
    int memo[2] = {0, 1};
    
    if (n < 2)
        return memo[n];

    int result;
    for (int i = 2; i <= n; i++) {
        result = memo[0] + memo[1];
        memo[0] = memo[1];
        memo[1] = result;
    }

    return result;
}

int main(int argc, char **argv)
{
    int N = atoi(argv[1]);
    printf("%d\n", fibonacci(N));
}
