package Impresa_Sportiva;

import java.util.Date;

public class Preparatore_Atletico extends Sportivo {
	
	Preparatore_Atletico(String Nome, String Cognome, Date Data_Assunzione, int Stipendio, int Numero_Iscrizione, int Numero_Reti, String TipologiaSportivo){
		super (Nome, Cognome, Data_Assunzione, Stipendio, Numero_Iscrizione, TipologiaSportivo);
		
	}
	
	public boolean Tipologia_Sportivo(Sportivo sportivo) {
		
		if (sportivo.TipologiaSportivo == "Preparatore_Atletico") {
			return true;
		}
		else {
			return false;
		}
	}

}
