import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = sc.nextInt();

        long [] visitNumber = new long[n];
        for (int i = 0; i < n; i++) {
            long x = sc.nextInt();
            visitNumber[i] = x;
        }

        long cnt = 0;
        for (int i = 0; i < k; i++) {
            cnt += visitNumber[i];
        }
        long maxCnt = cnt;
        // System.out.println("cnt: " + cnt);
        int day = 1;
        for (int i = 1; i <= n - k; i++) {
            cnt -= visitNumber[i - 1];
            cnt += visitNumber[i + k - 1];
            // System.out.println("i: " + i + "/ i + k -1: " + (i + k -1) + "/cnt: " + cnt);
            if (cnt == maxCnt) {
                day++;
            }
            // day = 1로 초기화 될 때는 현재 maxCnt보다 클 때만 초기화해여한다,
            // 작으면 유지해여함
            else if (cnt > maxCnt) {
                day = 1;
                maxCnt = cnt;
            } 
        }   
        if (maxCnt != 0) {
        System.out.println(maxCnt);
        System.out.println(day);
        }else {
            System.out.println("SAD");
        }

    }

}