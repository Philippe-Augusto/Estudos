#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

// Funcao que troca os valores referidos por x e y
void swap(int *x, int *y) {
    int temp = *x;

    *x = *y;
    *y = temp;
}

// Funcao que implementa a ordenacao por troca (bubble sort)
void bubbleSort(int arr[], int n) {
    for(int i=0; i<n-1; i++)
        // Os ultimos 'i' elementos ja estao em ordem
        for(int j=0; j<n-i-1; j++)
            if(arr[j] > arr[j+1])
                swap(&arr[j], &arr[j+1]);
}

// Funcao que implementa a ordenacao quick sort
void quickSort(int valor[], int esquerda, int direita) {
    int i, j, x, y;

    i = esquerda;
    j = direita;
    x = valor[(esquerda + direita) / 2];

    while(i <= j) {	
        while(valor[i]<x && i<direita)
            i++;

        while(valor[j]>x && j>esquerda)
            j--;

        if(i <= j) {
            y = valor[i];
            valor[i] = valor[j];
            valor[j] = y;
            i++;
            j--;
        }
    }

    if(j > esquerda)
        quickSort(valor, esquerda, j);
   
    if(i < direita)
        quickSort(valor, i, direita);
}

void imprimeArray (int array[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
}

int main() {

    pid_t pid = fork();

    int array[10] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};

    if(pid < 0) {
        fprintf(stderr, "Fork falhou\n");
        return 1;
    }

    if(pid == 0) { /* Processo filho */
        printf("Processo filho: Valor da variavel \"pid\" = %d\n", pid);
        quickSort(array, 10, 1);
        printf("Vetor ordenado QUICK SORT:");
        imprimeArray(array, 10);
    }
    else { 
        /* Processo pai */
        /* Pai aguardara filho completar */
        printf("Processo pai: Valor da variavel \"pid\" = %d\n", pid);
        wait(NULL);
        printf("Processo pai: Filho completou\n");
        bubbleSort(array, 10);
        printf("Vetor ordenado BUBBLE SORT:");
        imprimeArray (array, 10);
    }
}
