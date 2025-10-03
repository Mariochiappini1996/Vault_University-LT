#include <stdio.h>

/*
 * Lista prototipi
 * */
char switch_case( char ); // va bene anche  char switch_case( char c );

void main(){
	char c = 'd', c_out;
	printf("%c - %c\n", c, switch_case(c) );
	
	c = 'E';
	printf("%c - %c\n", c, switch_case(c) );
	
	c = '0';
	c_out = switch_case(c);
	if( c_out == -1)
		printf("%c non e' una lettera\n", c);
	else
		printf("%c - %c\n", c, c_out );
}

char switch_case(char c) { // Definizione della funzione 'switch_case' che prende un carattere come input

    if (c >= 'A' && c <= 'Z') { // Verifica se il carattere è una lettera maiuscola (ASCII tra 'A' e 'Z')                                                                       		return 'a' + c - 'A';// Converte il carattere maiuscolo in minuscolo sottraendo la differenza tra 'a' e 'A'

    }
    
    else if (c >= 'a' && c <= 'z') { // Verifica se il carattere è una lettera minuscola (ASCII tra 'a' e 'z')
           return 'A' + c - 'a'; // Converte il carattere minuscolo in maiuscolo sottraendo la differenza tra 'A' e 'a'

    }
        else { // Se il carattere non è né maiuscolo né minuscolo, restituisce -1

        return -1;
    }
}
