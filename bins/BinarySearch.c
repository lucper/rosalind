#include <string.h>
#include <stdlib.h>
#include <stdio.h>

int binsearch(int *arr, int start, int end, int key)
{
    int mid = (start + end) / 2;
    if (start == end && key != arr[mid])
        return -1;
    else if (key > arr[mid])
        return binsearch(arr, mid + 1, end, key);
    else if (key < arr[mid])
        return binsearch(arr, start, mid, key);
    else
        return mid;
}

static void str2int(int *buffer, char *items) {
    char *token = strtok(items, " ");
    for (int i = 0; token != NULL; i++) {
        buffer[i] = atoi(token);
        token = strtok(NULL, " ");
    }
}

int main(int argc, char **argv)
{
    size_t size= 0; // ignore
    char *currline = NULL;
    
    getline(&currline, &size, stdin);
    int n = atoi(currline);

    getline(&currline, &size, stdin);
    int m = atoi(currline);

    getline(&currline, &size, stdin);
    currline[strcspn(currline, "\n\r")] = 0; // replaces newline (if exists) by 0
    int arr[n];
    str2int(arr, currline);

    getline(&currline, &size, stdin);
    currline[strcspn(currline, "\n\r")] = 0; // replaces newline (if exists) by 0
    int keys[m];
    str2int(keys, currline);

    int idx;
    for (int i = 0; i < m; i++)
        printf("%d ", (idx = binsearch(arr, 0, n-1, keys[i])) > -1 ? idx+1 : -1); // format output as requested
    printf("\n");
}
