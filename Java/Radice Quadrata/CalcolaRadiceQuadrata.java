import java.util.Scanner;

public class CalcolaRadiceQuadrata {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Inserisci un numero: ");
        double numero = input.nextDouble();

        // Calcola la radice quadrata
        double radiceQuadrata = Math.sqrt(numero);

        System.out.println("La radice quadrata di " + numero + " è: " + radiceQuadrata);

        input.close();
    }
}
