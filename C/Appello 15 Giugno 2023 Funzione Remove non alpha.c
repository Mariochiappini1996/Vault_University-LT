#include <stdio.h>

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
    char input[] = "Hello,123 World!";
    printf("Input: %s\n", input);
    
    remove_non_alpha(input);
    
    printf("Output: %s\n", input);
    
    return 0;
}
