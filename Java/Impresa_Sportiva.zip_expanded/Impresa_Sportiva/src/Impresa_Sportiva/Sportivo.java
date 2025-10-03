package Impresa_Sportiva;

import java.util.Date;

public class Sportivo {
	
	public String Nome;
	public String Cognome;
	private Date Data_Assunzione;
	private int Stipendio;
	private String Numero_Iscrizione;
	public String TipologiaSportivo;
  
	
    Sportivo(String Nome, String Cognome, Date Data_Assunzione, int Stipendio, int Numero_Iscrizione, String TipologiaSportivo){
		
		this.Nome = Nome;
		this.Cognome = Cognome;
		this.Data_Assunzione = Data_Assunzione;
		this.Stipendio = Stipendio;
		this.TipologiaSportivo = TipologiaSportivo;
        this.Numero_Iscrizione = "TEAM_" + Numero_Iscrizione++;
        
	}
    
    public String getNome() {
        return Nome;
    }

    public void setNome(String Nome) {
        this.Nome = Nome;
    }

    public String getCognome() {
        return Cognome;
    }

    public void setCognome(String Cognome) {
        this.Cognome = Cognome;
    }

    public Date getData_Assunzione() {
        return Data_Assunzione;
    }

    public void setData_Assunzione(Date Data_Assunzione) {
        this.Data_Assunzione = Data_Assunzione;
    }

    public int getStipendio() {
        return Stipendio;
    }

    public void setStipendio(int Stipendio) {
        this.Stipendio = Stipendio;
    }

    public String getNumero_Iscrizione() {
        return Numero_Iscrizione;
    }
	
}
