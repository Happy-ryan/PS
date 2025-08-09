import java.io.*;
import java.util.*;

class Solution {
    public static int solution(int N, int d, int k, int c, int[] sushis) {
        int uniqueTypes = 0;
        // 회전 -> 같은 배열 2배로 만들어야함..
        int[] sushiRail = new int[2 * N];
        for (int i = 0; i < N; i++) {
            sushiRail[i] = sushis[i];
        }
        for (int i = N; i < 2 * N; i++) {
            sushiRail[i] = sushis[i - N];
        }

        Map<Integer, Integer> sushiSet = new HashMap<>();
        for (int i = 0; i < N; i++) {
            sushiSet.put(sushiRail[i], 0);
        }
        for (int i = 0; i < k; i++) {
            sushiSet.put(sushiRail[i], sushiSet.getOrDefault(sushiRail[i], 0) + 1);
            if (sushiSet.get(sushiRail[i]) == 1) {
                uniqueTypes++; // 1일 때만 더해서 종류 관리
            }
        }
        
        int maxVal = uniqueTypes;
        if (sushiSet.getOrDefault(c, 0) == 0) {
            maxVal++;
        }

//        System.out.println("초밥 구성 상태 : "+ initSushi);
//        System.out.println("최대 종류 : " + calSushi(initSushi, c, d));
//        System.out.println("=====");
        for (int i = 1; i < N; i++) {
//            System.out.println("시작 : " + i);
            int l = sushiSet.get(sushiRail[i - 1]) - 1;
            sushiSet.put(sushiRail[i - 1], l);
            if (l == 0) {
                uniqueTypes--;
                ;
            }
            int r = sushiSet.get(sushiRail[i + k - 1]) + 1;
            sushiSet.put(sushiRail[i + k - 1], r);
            if (r == 1) {
                uniqueTypes++;
            }

            int curVal = uniqueTypes;
            if (1 <= c && c <= d && !sushiSet.containsKey(c) || sushiSet.get(c) == 0) {
                curVal++;
            }
//            System.out.println("초밥 구성 상태 : "+ initSushi);
//            System.out.println("최대 종류 : " + calSushi(initSushi, c, d));
            maxVal = Math.max(maxVal, curVal);
//            System.out.println("=====");
        }
        return maxVal;

    }

    // 초밥 종류 세는 것도 윈도우로 관리!! <- 시간초과!!
    static int calSushi(Map<Integer, Integer> sushiSet, int coupon, int d) {
        int val = 0;
        for (int key : sushiSet.keySet()) {
            if (sushiSet.get(key) > 0) {
                val++;
            }
        }
        // 1 ~ d 안의 초밥 중에서 현재 레일에 없는 경우
        if (1 <= coupon && coupon <= d && !sushiSet.containsKey(coupon) || sushiSet.get(coupon) == 0) {
            val++;
        }
        return val;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        int[] sushis = new int[N];
        for (int i = 0; i < N; i++) {
            sushis[i] = Integer.parseInt(br.readLine());
        }

        System.out.println(Solution.solution(N, d, k, c, sushis));
        br.close();
    }
}