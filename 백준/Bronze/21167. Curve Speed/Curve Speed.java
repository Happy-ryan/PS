import java.io.*;
import java.util.*;

class Solution {
    public double solution(int R, double S) {
        S = Double.parseDouble("0" + S);
        double V = Math.sqrt((R * (S + 0.16)) / 0.067);
        return V;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Solution sol = new Solution();
        String input;

        while ((input = br.readLine()) != null && !input.isEmpty()) {
            StringTokenizer st = new StringTokenizer(input);
            int R = Integer.parseInt(st.nextToken());
            double S = Double.parseDouble(st.nextToken()); 

            double V = sol.solution(R, S);
            System.out.println(Math.round(V));
        }
    }
}
