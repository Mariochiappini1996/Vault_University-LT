#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct object {
	char type; // 'i', 'c' ed 's' per int, char e stringa
	void *pointer; //puntatore
};
typedef struct object object;


void set(object*, int, object);//Funzione set

void main(){
	object L[10];
	char a[] = "programmazione";
	int i;
	
	//Definisco nelle prime tre posizioni elementi di type diverso
	L[0].pointer = malloc(sizeof(int)); //int
	L[0].type = 'i';
	*(   (int*)(L[0].pointer)    ) = 3;
	
	L[1].pointer = malloc(sizeof(char)); //char
	L[1].type = 'c';
	*(   (char*)(L[1].pointer)    ) = 'x';
	
	L[2].pointer = (void*)a; //stringa
	L[2].type = 's';
	
	printf("[");
	for(i = 0; i < 3; i++){
		if( L[i].type == 'i' )
			printf("%d ", *((int*)L[i].pointer));
		else if ( L[i].type == 'c' )
			printf("%c ", *((char*)L[i].pointer));
		else printf("%s ", (char*)L[i].pointer );
	}
	printf("]\n");
}

void set(object *L, int p, object e){ //in ordine, lista posizione ed elemento
	L[p].type = e.type;
	if (L[p].type == 'i'){
		L[p].pointer = malloc(sizeof(int));
		*((int*)(L[p].pointer)) = *((int*)e.pointer);
	} else if (L[p].type == 'c'){
		L[p].pointer = malloc(sizeof(char));
		*((char*)(L[p].pointer)) = *((char*)e.pointer);
	} else {// é¨ una stringa
		L[p].pointer = malloc( sizeof(char)*(strlen((char*)e.pointer)+1) ); //Lunghezza stringa
		strcpy( e.pointer, L[p].pointer); //copia stringa
	}
}
