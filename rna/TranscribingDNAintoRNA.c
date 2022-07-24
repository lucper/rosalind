#include <string.h>
#include <stdio.h>
#include <stdlib.h>

void transcribe(char *buffer, const char *dna)
{
    strcpy(buffer, dna);
    for (int i = 0; i < strlen(dna); i++)
        if (dna[i] == 'T')
            buffer[i] = 'U';
}

int main(int argc, char **argv)
{
    size_t size = 0; // ignore
    char *dna = NULL;
    getline(&dna, &size, stdin);

    dna[strcspn(dna, "\n\r")] = 0; // replaces newline (if exists) by 0

    char rna[strlen(dna)];
    transcribe(rna, dna);
    printf("%s\n", rna);

    free(dna);
}
