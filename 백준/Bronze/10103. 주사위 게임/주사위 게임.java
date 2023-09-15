import java.io.*;
import java.util.*;

public class Main {
    public static int p1 = 100, p2 = 100;
    
    public static void verseScore(int score1, int score2) {
        if (score1 > score2)
            p2 -= score1;
        else if (score1 < score2)
            p1 -= score2;
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int score1 = Integer.parseInt(st.nextToken());
            int score2 = Integer.parseInt(st.nextToken());
            verseScore(score1, score2);
        }
        System.out.println(p1);
        System.out.println(p2);
    }
}