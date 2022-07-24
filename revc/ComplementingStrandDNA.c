#include <string.h>
#include <stdio.h>
#include <stdlib.h>

void reverse_complement(char *buffer, const char *dna)
{
    strcpy(buffer, dna);
    int lastindex = strlen(dna) - 1;
    for (int i = lastindex; i >= 0; i--)
        if (dna[i] == 'A')
            buffer[lastindex - i] = 'T';
        else if (dna[i] == 'T')
            buffer[lastindex - i] = 'A';
        else if (dna[i] == 'G')
            buffer[lastindex - i] = 'C';
        else if (dna[i] == 'C')
            buffer[lastindex - i] = 'G';
}

int main(int argc, char **argv)
{
    size_t size = 0; // ignore
    char *dna = NULL;
    getline(&dna, &size, stdin);

    dna[strcspn(dna, "\n\r")] = 0; // replace newline (if exists) by 0

    char revc[strlen(dna)];
    reverse_complement(revc, dna);

    printf("%s\n", revc);

    free(dna);
}
