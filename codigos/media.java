import java.io.*;
public class Media {
    public static void main(String[] args) {
        BufferedReader  inReader;
        inReader = new BufferedReader(new InputStreamReader(System.in));
        String line;
        int numero1, numero2 = 0;
        double media = 0;
        try {
            System.out.print("Digite o primeiro número: ");
            line = inReader.readLine();
            numero1 = Integer.parseInt(line);
            System.out.print("Digite o segundo número: ");
            line = inReader.readLine();
            numero2 = Integer.parseInt(line);
            media = (numero1 + numero2) / 2.0;
            System.out.println("A média é " + media);
            inReader.close();
        } catch (IOException e) {
            System.err.println(e.getMessage());
        }
    }
}