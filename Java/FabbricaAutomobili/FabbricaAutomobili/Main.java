package FabbricaAutomobili;

public class Main {
    public static void main(String[] args) {
        // Ipotizzo di creare dei componenti per soddisfare le esigenze del professor Stellato.
        Componente c1 = new Componente("Motore", "Italia", 2, 5000, null);
        Componente c2 = new Componente("Sospensioni", "Svizzera", 1, 100, null);
        Componente c3 = new Componente("Vernice", "Francia", 1.5, 200, null);
        Componente c4 = new Componente("Viti", "Germania", 2, 5000, null);
        Componente c5 = new Componente("Bulloni", "Germania", 1, 100, null);
        Componente c6 = new Componente("Specchietti", "Spagna", 1.5, 200, null);
        // Una volta che ho creato dei componenti mi dedico alla creazione di almeno due prodotti, in questo caso sono una macchina sportiva con identificativo 001 (P1)
        // ed una macchina Economica con identificativo 002 (P2). 
        Prodotto p1 = new Prodotto("P001", "Auto Sportiva", 5, 4);
        p1.aggiungiComponente(c1);
        p1.aggiungiComponente(c2);
        p1.aggiungiComponente(c3);
        p1.aggiungiComponente(c4);
        p1.aggiungiComponente(c5);
        p1.aggiungiComponente(c6);
// In modo del tutto casuale assegno dei componenti per creare questi due prototipi
        Prodotto p2 = new Prodotto("P002", "Auto Economica", 3, 4);
        p2.aggiungiComponente(c2);
        p2.aggiungiComponente(c3);
        p2.aggiungiComponente(c6);

        // Non tutte le fabbriche sono uguali, pertanto creo una nuova fabbrica al quale assegnare questi due nuovi prodotti
        Fabbrica fabbrica = new Fabbrica(50, 0.2);
        fabbrica.aggiungiProdotto(p1);
        fabbrica.aggiungiProdotto(p2);

        // Possiamo stampare i prodotti assegnati.
        fabbrica.stampaProdotti();

        // Creiamo la clausola per il miglior prodotto, attraverso un concetto di poliformismo ci agganciamo alla classe prodotto per estrapolare il metodo miglior ranking cambiando pero i parametri
        // e stampando in questo caso soltanto l'etichetta ( vediamola come se fosse una descrizione prodotto )
        Prodotto migliorProdotto = fabbrica.getProdottoConMigliorRanking();
        System.out.println("Prodotto con miglior ranking: " + migliorProdotto.getEtichetta());
    }
}


// Prodotto: Auto Sportiva
//Prezzo: 51300.0
//Componenti:
//- Motore - Sospensioni - Vernice - Viti - Bulloni - Specchietti
//Prodotto: Auto Economica
//Prezzo: 2670.0
//Componenti: - Sospensioni - Vernice - Specchietti
//Prodotto con miglior ranking: Auto Sportiva