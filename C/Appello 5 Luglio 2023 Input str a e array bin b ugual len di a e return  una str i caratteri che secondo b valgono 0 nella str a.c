#include <stdio.h>
#include <string.h>

void filtra(char *a, int *b) {
    int len = strlen(a);
    int char_filtro = 0;  // Indice per scrivere i caratteri filtrati

    for (int i = 0; i < len; i++) {
        if (b[i] == 1) {
            a[char_filtro] = a[i];
            char_filtro++;
        }
    }

    // Termina la stringa risultante
    a[char_filtro] = '\0';
}

int main() {
    char a[] = "algoritmo";
    int b[] = {0, 0, 0, 1, 0, 0, 1, 0, 1};
    
    filtra(a, b);

    printf("Risultato: %s\n", a);  // Stampa il risultato "oto"

    return 0;
}
