package Impresa_Sportiva;

import java.util.Date;
import java.util.HashMap;

public class Giocatore extends Sportivo {
	
	HashMap<String, Integer> Reti_per_Mese;
	
	
	Giocatore(String Nome, String Cognome, Date Data_Assunzione, int Stipendio, int Numero_Iscrizione, String TipologiaSportivo){
		super (Nome, Cognome, Data_Assunzione, Stipendio, Numero_Iscrizione, TipologiaSportivo);
		this.Reti_per_Mese = new HashMap <> ();
			
	}

	
	// Associa Numero di Reti a Mese solo per i Giocatori
    
		public void Numero_Reti() {
			if (TipologiaSportivo.equals("Giocatore")){
				
			Reti_per_Mese = new HashMap<>();
	        String[] mesi = {"Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"};
	       
	        for (String Mese : mesi) {
	            Reti_per_Mese.put(Mese, 0);
	        }
			}
	    }
	
		//Stampo vero se la tipologia di sportivo è GIOCATORE
		
		public boolean Tipologia_Sportivo(Sportivo sportivo) {
			
			if (sportivo.TipologiaSportivo == "Giocatore") {
				return true;
			}
			else {
				return false;
			}
		}
}
