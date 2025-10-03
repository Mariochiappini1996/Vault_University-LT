package FabbricaAutomobili;

//Stati(Attributi) di un componente
class Componente {
    private String nomeDelComponente;
    private String paeseDiProvenienza;
    private double tempoOrdinazione;
    private double costo;
    
// Progettiamo un costruttore
    public Componente(String nomeDelComponente, String paeseProvenienza, double tempoOrdinazione, double costo, String paeseDiProvenienza) {
        this.nomeDelComponente = nomeDelComponente;
        this.paeseDiProvenienza = paeseDiProvenienza;
        this.tempoOrdinazione = tempoOrdinazione;
        this.costo = costo;
    }
// Comportamenti correlati al mondo esterno (Metodi) in questo caso utilizziamo un getter per modularli

    public String getNome() {
        return nomeDelComponente;
    }

    public String getPaeseProvenienza() {
        return paeseDiProvenienza;
    }
    
    public double getCosto() {
        return costo;
    }
    
    public double getTempoOrdinazione() {
        return tempoOrdinazione;
    }

}


// La classe componente non utilizza principi fondamentali come ereditarietà o Poliformismo
// poichè si presenta come una classe concreta, non astratta, base e con soli metodi getter.