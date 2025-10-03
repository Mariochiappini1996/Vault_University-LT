#include <stdio.h>
#include <stdlib.h> //Libreria per implementare sizeof

void change_array(int x[], int n); //Prototipo funzione Change
int *copy_array( int *x, int n ); // Prototipo funzione copy
int *append_array( int *x, int n, int e ); // Prototipo funzione append


void main(){
	int d[15] = {0, 10, 20, 30, 40};
	int i, len_d = sizeof(d)/sizeof(int);
	int *p;
	int b[10] = {1,2};
	int len_b = sizeof(b)/sizeof(int);
	int len_p;
	
	
	change_array(d, len_d);
	for(i = 0; i < len_d; i++){
		printf("%d, ", d[i]);
	}
	printf("\n");
	
	p = copy_array(d, len_d);
	len_p = len_d;
	if (p != NULL) {
		for(i = 0; i < len_d; i++){
			printf("%d, ", p[i]);
		}
		printf("\n");
	} else {
		printf("Errore di memoria\n");
	}
	p = append_array(p, len_p, 100);
	len_p++;
	if (p != NULL) {
		for(i = 0; i < len_p; i++){
			printf("%d, ", p[i]);
		}
		printf("\n");
	} else {
		printf("Errore di memoria\n");
	}
}

// Definizione della funzione 'append_array' che aggiunge un elemento a un array di interi
int *append_array(int *x, int n, int e) {
    // Dichiarazione della variabile di iterazione
    int i;
    
    // Alloca memoria dinamicamente per un nuovo array di interi con un elemento aggiuntivo
    int *a = malloc((n + 1) * sizeof(int));
    
    // Verifica se l'allocazione di memoria è andata a buon fine
    if (a != NULL) {
        // Ciclo per copiare gli elementi da 'x' al nuovo array appena allocato 'a'
        for (i = 0; i < n; i++) {
            a[i] = x[i]; // Copia l'i-esimo elemento da 'x' all'array 'a'
        }
        
        // Aggiunge l'elemento 'e' all'ultimo indice del nuovo array 'a'
        a[n] = e;
    }
    
    // Libera la memoria dell'array originale 'x', poiché è stato copiato in 'a'
    free(x);
    
    // Restituisce il puntatore al nuovo array 'a' con l'elemento aggiunto
    return a;
}


// Definizione della funzione 'copy_array' che copia un array di interi
int *copy_array(int *x, int n) {
    // Dichiarazione della variabile di iterazione
    int i;
    
    // Alloca memoria dinamicamente per un nuovo array di interi
    int *a = malloc(n * sizeof(int));
    
    // Verifica se l'allocazione di memoria è andata a buon fine
    if (a != NULL) {
        // Ciclo per copiare gli elementi da 'x' all'array appena allocato 'a'
        for (i = 0; i < n; i++) {
            // Copia l'i-esimo elemento da 'x' all'array 'a'
            a[i] = x[i]; // Copia l'elemento i-esimo
        }
    }
    
    // Restituisce il puntatore all'array copiato 'a'
    return a;
}

// Definizione della funzione 'change_array' che modifica gli elementi di un array di interi
void change_array(int x[], int n) {
    // Dichiarazione della variabile di iterazione
    int i;
    
    // Ciclo per iterare attraverso gli elementi dell'array 'x'
    for (i = 0; i < n; i++) {
        // Modifica l'i-esimo elemento dell'array 'x'
        // Assegna il valore 10 * i all'elemento i-esimo dell'array 'x'
        x[i] = 10 * i;
    }
}
