#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#define MAXLINES 2
#define MAXBASES 1000

int hamming(const char *dna1, const char *dna2)
{
    int dist = 0;
    for (int i = 0; i < strlen(dna1); i++)
        if (dna1[i] != dna2[i])
            dist++;
    return dist;
}

int main(int argc, char **argv)
{
    size_t size = 0; // ignore
    char *currline = NULL;

    char strands[MAXLINES][MAXBASES];
    for (int i = 0; getline(&currline, &size, stdin) >= 0 && i < MAXLINES; i++) {
        currline[strcspn(currline, "\n\r")] = 0;
        strcpy(strands[i], currline);
    }

    printf("%d\n", hamming(strands[0], strands[1]));
        
    free(currline);
}
