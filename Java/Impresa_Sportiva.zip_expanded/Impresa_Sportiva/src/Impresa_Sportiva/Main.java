package Impresa_Sportiva;

import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Sportivo> sportivi = new ArrayList<>();

        // Creazione di alcuni sportivi per testare le funzionalità
        Giocatore giocatore1 = new Giocatore("Mario", "Rossi", new Date(120, 0, 10), 3, 1, "Giocatore");
        Giocatore giocatore2 = new Giocatore("Giovanni", "Bianchi", new Date(121, 0, 15), 4, 2, "Giocatore");
        Medico medico1 = new Medico("Sara", "Verdi", new Date(121, 2, 20), 2, 3, 0, "Medico");
        Medico medico2 = new Medico("Laura", "Neri", new Date(121, 2, 25), 3, 4, 0, "Medico");
        Allenatore allenatore1 = new Allenatore("Paolo", "Bruni", new Date(120, 5, 30), 5, 5, 0, "Allenatore");
        
        sportivi.add(giocatore1);
        sportivi.add(giocatore2);
        sportivi.add(medico1);
        sportivi.add(medico2);
        sportivi.add(allenatore1);

        // Aggiunta di reti per i giocatori
        giocatore1.Numero_Reti();
        giocatore1.Reti_per_Mese.put("Gennaio", 3);
        giocatore1.Reti_per_Mese.put("Febbraio", 1);
        giocatore1.Reti_per_Mese.put("Marzo", 2);

        giocatore2.Numero_Reti();
        giocatore2.Reti_per_Mese.put("Gennaio", 2);

        int retiMinime = 2;
        stampaGiocatoriConReti(sportivi, retiMinime);
        stampaSportiviAssuntiStessoMeseAnno(sportivi);
    }

    public static void stampaGiocatoriConReti(List<Sportivo> sportivi, int retiMinime) {
        for (Sportivo sportivo : sportivi) {
            if (sportivo instanceof Giocatore && sportivo.getStipendio() >= 3) {
                Giocatore giocatore = (Giocatore) sportivo;
                int mesiConReti = 0;
                for (int reti : giocatore.Reti_per_Mese.values()) {
                    if (reti >= retiMinime) {
                        mesiConReti++;
                    }
                }
                if (mesiConReti > 0) {
                    System.out.println(giocatore.getNome() + " " + giocatore.getCognome() + " " + mesiConReti);
                }
            }
        }
    }

    public static void stampaSportiviAssuntiStessoMeseAnno(List<Sportivo> sportivi) {
        HashMap<String, List<Sportivo>> mappaAssunzioni = new HashMap<>();

        for (Sportivo sportivo : sportivi) {
            Date data = sportivo.getData_Assunzione();
            String chiave = (data.getYear() + 1900) + "-" + (data.getMonth() + 1);

            if (!mappaAssunzioni.containsKey(chiave)) {
                mappaAssunzioni.put(chiave, new ArrayList<>());
            }
            mappaAssunzioni.get(chiave).add(sportivo);
        }

        for (String chiave : mappaAssunzioni.keySet()) {
            List<Sportivo> assunti = mappaAssunzioni.get(chiave);
            if (assunti.size() > 1) {
                HashMap<String, Integer> tipiAssunzioni = new HashMap<>();
                for (Sportivo sportivo : assunti) {
                    String tipo = sportivo.TipologiaSportivo;
                    tipiAssunzioni.put(tipo, tipiAssunzioni.getOrDefault(tipo, 0) + 1);
                }
                for (String tipo : tipiAssunzioni.keySet()) {
                    if (tipiAssunzioni.get(tipo) > 1) {
                        System.out.println("Mese/Anno: " + chiave + " - Tipo: " + tipo + " - Numero: " + tipiAssunzioni.get(tipo));
                    }
                }
            }
        }
    }
}

