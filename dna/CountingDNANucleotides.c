#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#define A 0
#define C 1
#define G 2
#define T 3

void count_bases(int *bases, const char *dna)
{
    for (int i = 0; i < strlen(dna); i++)
        if (dna[i] == 'A')
            bases[A]++;
        else if (dna[i] == 'C')
            bases[C]++;
        else if (dna[i] == 'G')
            bases[G]++;
        else if (dna[i] == 'T')
            bases[T]++;
}

int main(int argc, char **argv)
{
    size_t size = 0; // ignore
    char *buffer = NULL;
    getline(&buffer, &size, stdin);

    buffer[strcspn(buffer, "\n")] = 0; // replace newline (if exists) by 0

    int bases[4] = {0, 0, 0, 0};
    count_bases(bases, buffer);
    printf("A: %d\nC: %d\nG: %d\nT: %d\n", bases[A], bases[C], bases[G], bases[T]);

    free(buffer);
}
