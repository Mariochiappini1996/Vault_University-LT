package FabbricaAutomobili;

import java.util.ArrayList;
import java.util.List;
// Stati(Attributi) di un prodotto
class Prodotto {
    private String identificativo;
    private String etichetta;
    private double tempoDiRealizzazione; // in giorni
    private List<Componente> componenti;
    private int numeroComponenti;
// Progettiamo un costruttore
    public Prodotto(String identificativo, String etichetta, double tempoDiRealizzazione, int numeroComponenti) {
        this.identificativo = identificativo;
        this.etichetta = etichetta;
        this.tempoDiRealizzazione = tempoDiRealizzazione;
        this.numeroComponenti = numeroComponenti;
        this.componenti = new ArrayList<>();
    }
// Ci serve poter inserire i componenti(In questo caso subcomponenti) per creare un prodotto. In altre parole un Metodo che mette in comunicazione la superclasse(genitore) prodotto con la sottoclasse componenti.
    public void aggiungiComponente(Componente componente) {
        componenti.add(componente);
    }
 // Comportamenti correlati al mondo esterno (Metodi) in questo caso utilizziamo un getter per modularli
    public String getIdentificativo() {
        return identificativo;
    }

    public String getEtichetta() {
        return etichetta;
    }

    public double getTempoDiRealizzazione() {
        return tempoDiRealizzazione;
    }

    public List<Componente> getComponenti() {
        return componenti;
    }

    public int getNumeroComponenti() {
        return numeroComponenti;
    }
 // Calcola il costo totale dei componenti del prodotto (Utilizzo il double per una maggior raffinazione del costo)
    public double calcolaCostoComponenti() {
        double costoTotale = 0;
        for (Componente c : componenti) {
            costoTotale += c.getCosto();
        }
        return costoTotale * numeroComponenti;
    }
    // Calcola il tempo totale per l'ordine dei componenti del prodotto (Utilizzo il double per una maggior raffinazione del tempo necessario)
    public double calcolaTempoTotale() {
        double tempoMaxOrdinazione = 0;
        for (Componente c : componenti) {
            if (c.getTempoOrdinazione() > tempoMaxOrdinazione) {
                tempoMaxOrdinazione = c.getTempoOrdinazione();
            }
        }
        return tempoMaxOrdinazione + tempoDiRealizzazione;
    }
    // Calcola il prezzo di vendita del prodotto
    public double calcolaCostoProduzione(double costoManodopera) {
        return calcolaCostoComponenti() + (calcolaTempoTotale() * costoManodopera);
    }
 // Calcola il costo di produzione del prodotto
    public double calcolaPrezzo(double costoManodopera, double fattoreGuadagno) {
        return calcolaCostoProduzione(costoManodopera) * (1 + fattoreGuadagno);
    }
}

// La classe prodotto include una lista di componenti (List<Componente>) e metodi per calcolare costi e tempi,
// questi ultimi mi fanno credere che vi siano due principi di astrattezza all'interno della classe.'