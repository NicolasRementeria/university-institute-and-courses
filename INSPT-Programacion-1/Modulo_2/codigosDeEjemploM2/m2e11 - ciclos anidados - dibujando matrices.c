#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i=0,j=0;

    printf("Graficando una matriz con ciclos while\n");
    while (i<5){
        j=0;
        while (j<10){
            //printf("i=%d|j=%d\t",i,j);
            printf("f(%d,%d)\t",i,j);
            j++;
        }
        printf("\n");
        i++;
    }

    printf("\nPero es mas simple con ciclos for\n");
    for (i=0;i<5;i++){
        for (j=0;j<10;j++){
            //printf("i=%d|j=%d\t",i,j);
            printf("f(%d,%d)\t",i,j);
        }
        printf("\n");
    }

    return 0;
}
