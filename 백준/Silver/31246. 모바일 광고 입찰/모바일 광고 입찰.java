

import java.io.*;
import java.util.*;

class Solution {
    public int solution(int N, int K, long[][] parts) {
        int answer = 0;
        int cnt = 0;

        List<Long> list = new ArrayList<>();

        for (long[] part : parts) {
            long A = part[0];
            long B = part[1];
            if (A >= B) {
                cnt++;
            } else {
                list.add(B - A);
            }
        }

        Collections.sort(list);
        
        int num = K - cnt;
        
        if (num <= 0) {
            return 0;
        }
        long x = list.get(num - 1);
        return (int) x;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        long[][] parts = new long[N][2];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            parts[i][0] = Long.parseLong(st.nextToken());
            parts[i][1] = Long.parseLong(st.nextToken());
        }

        int answer = new Solution().solution(N, K, parts);
        System.out.println(answer);
    }
}

