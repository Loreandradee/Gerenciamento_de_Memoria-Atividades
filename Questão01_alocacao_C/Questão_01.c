#include <stdio.h>  
#include <stdlib.h> 

int main() {
    
    //  ==== Alocação Estática ====
    printf("--- 1. Alocação Estática ---\n");
    
    // Declare um array estático de 5 inteiros.
    int arr_estatico[5];
    
    for (int i = 0; i < 5; i++) {
        arr_estatico[i] = i + 1;
        printf("arr_estatico[%d] = %d\n", i, arr_estatico[i]);
    }
    
    //  ==== Alocação Dinâmica  ====
    printf("\n ==== 2. Alocação Dinâmica  ====\n");
    
    int *arr_dinamico; // Ponteiro que apontará para a memória no heap.
    int n_dinamico = 10;
    
    // Aloque dinamicamente um array de 10 inteiros usando malloc.
    arr_dinamico = (int *)malloc(n_dinamico * sizeof(int));
    
    // Verificação de Sucesso:
    if (arr_dinamico == NULL) {
        printf("Erro! Falha ao alocar memória dinâmica no heap.\n");
        return 1; // Encerra o programa indicando um erro.
    } else {
        printf("Memória dinâmica alocada com sucesso!\n");
    }
    
    // Preencha o array dinâmico com valores de 10 a 19.
    for (int i = 0; i < n_dinamico; i++) {
        arr_dinamico[i] = i + 10;
        printf("arr_dinamico[%d] = %d\n", i, arr_dinamico[i]);
    }
    
    //  ==== Comparação de Endereços  ====
    printf("\n ==== 4 e 5. Comparação de Endereços  ====\n");
    
    // Imprima os endereços de memória (base) de ambos os arrays.
    
    printf("Endereço base do array estático (Stack): %p\n", (void *)arr_estatico);
    printf("Endereço base do array dinâmico (Heap):   %p\n", (void *)arr_dinamico);
    
    // Calcule e exiba a diferença entre os endereços.
 
    long diferenca = labs((long)arr_dinamico - (long)arr_estatico);
    
    printf("Distância (diferença absoluta) entre os endereços: %ld bytes\n", diferenca);
    printf("(Isso demonstra que estão em regiões de memória distintas)\n");
    
    //  ==== Liberação de Memória  ====
    printf("\n ==== 6. Liberação de Memória  ====\n");
    
    // Libere a memória alocada dinamicamente.
    free(arr_dinamico);
    arr_dinamico = NULL; 
                         
    printf("Memória dinâmica liberada com sucesso.\n");
    
    return 0; // programa terminou.
}