import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());

            ArrayList<Integer>[] adj = new ArrayList[N + 1];
            int[] ind = new int[N + 1];
            int[] dp = new int[N + 1];
            int[] times = new int[N + 1];

            StringTokenizer timeTokens = new StringTokenizer(br.readLine());
            for (int j = 1; j <= N; j++) {
                times[j] = Integer.parseInt(timeTokens.nextToken());
                adj[j] = new ArrayList<>();
            }

            for (int j = 0; j < K; j++) {
                st = new StringTokenizer(br.readLine());
                int X = Integer.parseInt(st.nextToken());
                int Y = Integer.parseInt(st.nextToken());
                adj[X].add(Y);
                ind[Y]++;
            }

            int W = Integer.parseInt(br.readLine());
            Queue<Integer> candidates = new LinkedList<>();

            for (int num = 1; num <= N; num++) {
                if (ind[num] == 0) {
                    candidates.add(num);
                    dp[num] = times[num];
                }
            }

            ArrayList<Integer> result = new ArrayList<>();
            while (!candidates.isEmpty()) {
                int cur = candidates.poll();
                result.add(cur);

                for (int nxt : adj[cur]) {
                    ind[nxt]--;
                    dp[nxt] = Math.max(dp[nxt], times[nxt] + dp[cur]);

                    if (ind[nxt] == 0) {
                        candidates.add(nxt);
                    }
                }
            }

            System.out.println(dp[W]);
        }
    }
}
