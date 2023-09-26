import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            adj.add(new ArrayList<>());
        }

        int[] ind = new int[n + 1];

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int[] nums = new int[st.countTokens()];
            for (int j = 0; st.hasMoreTokens(); j++) {
                nums[j] = Integer.parseInt(st.nextToken());
            }
            for (int j = 1; j < nums.length - 1; j++) {
                adj.get(nums[j]).add(nums[j + 1]);
                ind[nums[j + 1]]++;
            }
        }

        List<Integer> candidates = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (ind[i] == 0) {
                candidates.add(i);
            }
        }

        List<Integer> result = new ArrayList<>();
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

        if (result.size() != n) {
            System.out.println(0);
        } else {
            for (int num : result) {
                System.out.println(num);
            }
        }
    }
}