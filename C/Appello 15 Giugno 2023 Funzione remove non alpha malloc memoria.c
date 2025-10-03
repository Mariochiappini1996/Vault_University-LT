#include <stdio.h>
#include <stdlib.h>

void remove_non_alpha(char *a) {
    if (a == NULL) {
        return; // Gestione caso in cui il puntatore sia NULL
    }
    
    int i, j;
    for (i = 0, j = 0; a[i] != '\0'; i++) {
        // Confronto se il carattere è tra 'A' e 'Z' o tra 'a' e 'z'
        if ((a[i] >= 'A' && a[i] <= 'Z') || (a[i] >= 'a' && a[i] <= 'z')) {
            a[j++] = a[i]; // Conserva solo caratteri alfabetici
        }
    }
    a[j] = '\0'; // Termina la stringa con il carattere nullo
}

int main() {
    char *input = (char *)malloc(100 * sizeof(char)); // Allocazione dinamica della memoria
    if (input == NULL) {
        return 1; // Uscita in caso di fallimento dell'allocazione
    }
    
    // Copia della stringa nell'area di memoria allocata
    snprintf(input, 100, "Hello,123 World!");
    
    printf("Input: %s\n", input);
    
    remove_non_alpha(input);
    
    printf("Output: %s\n", input);
    
    free(input); // Libera la memoria allocata
    
    return 0;
}


#include <stdio.h>

int main(int argc, char **argv)
{
	
	return 0;
}

