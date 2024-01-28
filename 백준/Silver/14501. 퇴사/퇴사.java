import java.util.*;

public class Main {
    public static int n;

    public static int[] dp;

    public static int[][] table;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        table = new int[n + 1][2];
        dp = new int[n + 1];
        for(int i = 1; i <= n; i++) {
            int time = sc.nextInt();
            int price = sc.nextInt();
            table[i][0] = time;
            table[i][1] = price;
            dp[i] = -1;
        }
        int maxVal = 0;
        for(int i = 1; i <= n; i++){
            // System.out.println(i + ":" + dpf(i));
            if (i + table[i][0] - 1 <= n){
                maxVal = Math.max(maxVal, dpf(i));
            }
        }
        System.out.println(maxVal);
    }
    //  시작점은 여러개가 된다! > 전수로 확인 필요!
    // dpf(n): n일에 그 일을 마지막으로 했을 때의 가능한 상담금액 합의 최대값
    // dpf(n) = max(dpf(i) where 0 <= i < n  
    // if i + table[i][0] - 1 < n: +table[n][1])
    public static int dpf(int n) {
        if (dp[n] != -1) {
            return dp[n];
        }

        int ret = 0;
        boolean isStart = true;
        for (int i = 1; i < n; i++) {
            if (i + table[i][0] - 1 < n) {
                ret = Math.max(ret, dpf(i) + table[n][1]);
                isStart = false;
            }
        }
        // 처음 선택한 날 빼고는 상담이 불가능할 때!
        if (isStart) {
            return table[n][1];
        }

        dp[n] = ret;

        return ret;
    }

}