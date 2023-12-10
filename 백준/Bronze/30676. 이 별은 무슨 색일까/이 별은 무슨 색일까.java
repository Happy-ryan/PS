import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        bw.write(printColor(n));
        bw.flush();
    }

    private static String printColor(int number) {
        if (620 <= number && number <= 780) {
            return "Red";
        }
        if (590 <= number && number < 620) {
            return "Orange";
        }
        if (570 <= number && number < 590) {
            return "Yellow";
        }
        if (495 <= number && number < 570) {
            return "Green";
        }
        if (450 <= number && number < 495) {
            return "Blue";
        }
        if (425 <= number && number < 450) {
            return "Indigo";
        }
        if (380 <= number && number < 425) {
            return "Violet";
        }
        return "ERROR";
    }
}