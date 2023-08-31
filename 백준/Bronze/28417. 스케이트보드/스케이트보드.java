import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int ans = 0;

        for (int i = 0; i < n; i++) {
            int[] scores = new int[7];
            for (int j = 0; j < 7; j++) {
                scores[j] = sc.nextInt();
            }
        

            int one = Math.max(scores[0], scores[1]);
            Arrays.sort(scores, 2, 7);
            int two = scores[6];
            int three = scores[5];

            ans = Math.max(ans, one + two + three);
        }

        System.out.println(ans);
    }
}