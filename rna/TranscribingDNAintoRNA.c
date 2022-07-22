#include <string.h>
#include <stdio.h>
#include <stdlib.h>

void transcribe(char *rna, const char *dna)
{
    strcpy(rna, dna);
    for (int i = 0; i < strlen(dna); i++)
        if (dna[i] == 'T')
            rna[i] = 'U';
}

int main(int argc, char **argv)
{
    size_t size = 0; // ignore
    char *buffer = NULL; // for DNA string
    getline(&buffer, &size, stdin);

    buffer[strcspn(buffer, "\n")] = 0; // replaces newline (if exists) by 0

    char rna[strlen(buffer)];
    transcribe(rna, buffer);
    printf("%s\n", rna);

    free(buffer);
}
