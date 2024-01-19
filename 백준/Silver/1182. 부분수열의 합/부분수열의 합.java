import java.io.*;
import java.util.*;

public class Main {
    
    private static int N, S, cnt;
    private static int[] used, nums;
    private static List<Integer> ans;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer inputNS = new StringTokenizer(br.readLine());

        N = Integer.parseInt(inputNS.nextToken());
        S = Integer.parseInt(inputNS.nextToken());

        used = new int[N];
        nums = new int[N];
        ans = new ArrayList<>();
        cnt = 0;

        StringTokenizer input = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(input.nextToken());
        }

        for (int k = 1; k <= N; k++) {
            dfs(0, 0, k);
        }

        System.out.println(cnt);
    }

    private static void dfs(int level, int idx, int k) {
        if (level == k) {
            if (sumList(ans) == S) {
                cnt++;
                return;
            } else {
                return;
            }
        }

        for (int i = idx; i < N; i++) {
            if (used[i] == 0) {
                used[i] = 1;
                ans.add(nums[i]);
                dfs(level + 1, i + 1, k);
                used[i] = 0;
                ans.remove(ans.size() - 1);
            }
        }
    }

    private static int sumList(List<Integer> list) {
        int sum = 0;
        for (int num : list) {
            sum += num;
        }
        return sum;
    }
}