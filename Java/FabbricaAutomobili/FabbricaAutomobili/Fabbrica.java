package FabbricaAutomobili;
// Avrò bisogno della classe prodotto, pertanto mi avvalgo della facoltà di importare Arraylist e List
import java.util.ArrayList;
import java.util.List;

class Fabbrica {
    private double costoManodopera; // Potremmo avere numeri con virgole, meglio utilizzare double
    private double fattoreGuadagno; // Potremmo avere numeri con virgole, meglio utilizzare double
    private List<Prodotto> prodotti; // Ho necessità di rendere prodotto una mia subclass per tenere traccia di stati e comportamenti
//Progettiamo un costruttore
    public Fabbrica(double costoManodopera, double fattoreGuadagno) {
        this.costoManodopera = costoManodopera;
        this.fattoreGuadagno = fattoreGuadagno;
        this.prodotti = new ArrayList<>();
    }
// CI servirà aggiungere dei prodotti all'interno della fabbrica.
    public void aggiungiProdotto(Prodotto prodotto) {
        prodotti.add(prodotto);
    }
//Possono servirci dei Metodi setter per aggiornare il costo della manodopera e il fattore di guadagno

    public void setCostoManodopera(double costoManodopera) {
        this.costoManodopera = costoManodopera;
    }

    public void setFattoreGuadagno(double fattoreGuadagno) {
        this.fattoreGuadagno = fattoreGuadagno;
    }

    public List<Prodotto> getProdotti() {
        return prodotti;
    }
// NOTA ?? questo comportamento correlato a come trovare il miglior ranking (astratto????) bisognerà implementarlo dentro il main per soddisfare una delle esigenze
    public Prodotto getProdottoConMigliorRanking() {
        Prodotto migliorProdotto = null;
        double migliorRanking = Double.MIN_VALUE;

        for (Prodotto p : prodotti) {
            double guadagno = p.calcolaPrezzo(costoManodopera, fattoreGuadagno) - p.calcolaCostoProduzione(costoManodopera);
            double tempoTotale = p.calcolaTempoTotale();
            double ranking = guadagno / tempoTotale;

            if (ranking > migliorRanking) {
                migliorRanking = ranking;
                migliorProdotto = p;
            }
        }

        return migliorProdotto;
    }
// mi serve avere delle informazioni ogni qualvolta facciamo un print in fabbrica
    public void stampaProdotti() {
        for (Prodotto p : prodotti) {
            System.out.println("Prodotto: " + p.getEtichetta());
            System.out.println("Prezzo: " + p.calcolaPrezzo(costoManodopera, fattoreGuadagno));
            System.out.println("Componenti:"); // Estraggo le componenti che mi servono per quel prodotto
            for (Componente c : p.getComponenti()) {
                System.out.println("- " + c.getNome());
                }
            }
        }
    }


// Anche questa classe come prodotto, mi fa credere che vi sia un concetto di astrattezza all'interno della classe, poichè eredita da prodotto i metodi costi e tempo.'