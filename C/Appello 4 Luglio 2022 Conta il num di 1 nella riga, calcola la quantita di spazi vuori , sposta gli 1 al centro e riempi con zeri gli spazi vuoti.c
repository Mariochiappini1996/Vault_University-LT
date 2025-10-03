#include <stdio.h>

void centering(int *a, int r, int c) {
    for (int i = 0; i < r; i++) {
        int count_uno = 0;
        int left_padding = 0;

        // Conta il numero di 1 nella riga
        for (int j = 0; j < c; j++) {
            if (a[i * c + j] == 1) {
                count_uno++;
            }
        }

        // Calcola la quantità di spazi vuoti a sinistra
        left_padding = (c - count_uno) / 2;

        // Sposta i 1 al centro e riempi con 0 gli spazi vuoti
        for (int j = 0; j < c; j++) {
            if (left_padding > 0) {
                a[i * c + j] = 0;
                left_padding--;
            } else if (count_uno > 0) {
                a[i * c + j] = 1;
                count_uno--;
            } else {
                a[i * c + j] = 0;
            }
        }
    }
}

int main() {
    int a[] = {
        1,1,0,0,0,
        1,0,0,0,0,
        1,1,1,0,0,
        1,1,0,0,0,
        1,1,1,1,0,
        1,1,1,1,1
    };
    int r = 6, c = 5;

    centering(a, r, c);

    // Stampa l'array risultante
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            printf("%d ", a[i * c + j]);
        }
        printf("\n");
    }

    return 0;
}
