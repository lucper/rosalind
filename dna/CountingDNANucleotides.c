#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#define A 0
#define C 1
#define G 2
#define T 3

void count_bases(int *buffer, const char *dna)
{
    for (int i = 0; i < strlen(dna); i++)
        if (dna[i] == 'A')
            buffer[A]++;
        else if (dna[i] == 'C')
            buffer[C]++;
        else if (dna[i] == 'G')
            buffer[G]++;
        else if (dna[i] == 'T')
            buffer[T]++;
}

int main(int argc, char **argv)
{
    size_t size = 0; // ignore
    char *dna = NULL;
    getline(&dna, &size, stdin);

    dna[strcspn(dna, "\n")] = 0; // replace newline (if exists) by 0

    int counter[4] = {0, 0, 0, 0};
    count_bases(counter, dna);
    printf("A: %d\nC: %d\nG: %d\nT: %d\n", counter[A], counter[C], counter[G], counter[T]);

    free(dna);
}
