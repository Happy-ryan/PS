import java.io.*;
import java.util.*;

public class Main {

    public static List<Integer> ans = new ArrayList<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        ArrayList<Integer> levels = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            levels.add(scanner.nextInt());
        }

        Collections.sort(levels, Collections.reverseOrder());

        int levelSum = 0;
        int unionSum = 0;

        for (int i = 0; i < 42; i++) {
            if (i >= n) {
                break;
            }

            levelSum += levels.get(i);

            if (levels.get(i) >= 250) {
                unionSum += 5;
            } else if (levels.get(i) >= 200) {
                unionSum += 4;
            } else if (levels.get(i) >= 140) {
                unionSum += 3;
            } else if (levels.get(i) >= 100) {
                unionSum += 2;
            } else if (levels.get(i) >= 60) {
                unionSum += 1;
            }
        }

        System.out.println(levelSum + " " + unionSum);

    } 

}