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

int main(int argc, char **argv)
{
    int arr[5] = {1,2,3,4,5};
    int key = 2;
    int indx = binsearch(arr, 0, 4, key);
    printf("2 is at index %d\n", indx);
}
