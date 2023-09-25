import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            adj.add(new ArrayList<>());
        }
        int[] ind = new int[n + 1];

        for (int i = 0; i < m; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            adj.get(x).add(y);
            ind[y]++;
        }

        ArrayList<Integer> candidates = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (ind[i] == 0) {
                candidates.add(i);
            }
        }

        ArrayList<Integer> result = new ArrayList<>();
        while (!candidates.isEmpty()) {
            int cur = candidates.remove(candidates.size() - 1);
            result.add(cur);

            for (int nxt : adj.get(cur)) {
                ind[nxt]--;
                if (ind[nxt] == 0) {
                    candidates.add(nxt);
                }
            }
        }

        for (int num : result) {
            System.out.print(num + " ");
        }
    }
}