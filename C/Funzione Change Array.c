#include <stdio.h>

void change_array(int x[], int n){ //change elemento in posizione definita dall indice di x nell array
	int i;
	for (i = 0; i < n; i++){
		x[i] = 10*i;
	}
}

void main(){
	int a[10]; // Array di 10 elementi non definiti
	int b[] = {0, 10, 20, 30, 40}; // Array con elementi definiti
	int c[5] = {0, 10, 20, 30, 40}; // Array definito 
	int d[15] = {0, 10, 20, 30, 40}; // Array definito in parte i successivi non definiti saranno 0
	int e[100] = {0}; // Array definito con un elemento 0, gli altri saranno tutti 0
	int i, len_d; // Inizializzo un contatore e il len (Lunghezza byte in C)
	
	d[11] = 21; //Aggiornamento elemento Array
	printf("%d, %d, %d, %d, %d, %d\n", a[4], b[0], c[2], d[10], e[97], d[11]); //STampo valori int indicizzati
	
	len_d = sizeof(d)/sizeof(int); //formulo la lunghezza di elementi di d
	
	printf("------ %d\n", len_d); // stampo in console la quantitá di elementi di d
	
	for(i = 0; i < len_d; i++){
		printf("%d\n", d[i]);
	}
	
	change_array(d, len_d);
	for(i = 0; i < len_d; i++){
		printf("%d\n", d[i]);
	}
	
}

