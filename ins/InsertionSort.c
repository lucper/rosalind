#include <string.h>
#include <stdlib.h>
#include <stdio.h>

void print_arr(int *arr, int size)
{
    for (int i = 0; i < size - 1; i++)
        printf("%d ", arr[i]);
    printf("%d\n", arr[size - 1]);
}

void insertion_sort(int *arr, int size)
{
    if (size > 1) {
        insertion_sort(arr, size - 1);
        int last = arr[size - 1];
        int j = size - 2;
        while (j >= 0 && last < arr[j]) {
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = last;
    }
}

int main(int argc, char **argv)
{
    size_t size = 0; // ignore
    char *buffer = NULL;
    getline(&buffer, &size, stdin);

    buffer[strcspn(buffer, "\n\r")] = 0; // replaces newline (if exists) by 0

    int number_items = 1; // to count last word
    for (int i = 0; i < strlen(buffer); i++)
        if (buffer[i] == ' ')
            number_items++;

    int arr[number_items], i = 0;

    char *token = strtok(buffer, " ");
    while (token != NULL) {
        arr[i++] = atoi(token);
        token = strtok(NULL, " ");
    }

    insertion_sort(arr, number_items);

    print_arr(arr, number_items);

    free(buffer);
}
