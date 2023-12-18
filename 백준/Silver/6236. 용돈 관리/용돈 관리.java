import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer inputNM = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(inputNM.nextToken());
        int M = Integer.parseInt(inputNM.nextToken());

        List<Integer> moneys = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            int money = Integer.parseInt(br.readLine());
            moneys.add(money);
        }
        System.out.println(getMinumWithdrawMoney(moneys, M));

    }

    private static int getMinumWithdrawMoney(List<Integer> moneys, int targetCount) {
        int l = Collections.max(moneys), r = 1000000000, ans = -1;
        while (l <= r) {
            int m = (l + r) / 2;
            // 인출 기준 금액이 클수록 인출 회수는 줄어든다.
            // 타겟 인출가 더 크다면 인출 기준 금액을 줄여야 한다.
            if (calculateWithdrawCount(moneys, m) <= targetCount) {
                r = m - 1;
                ans = m;
            } else {
                l = m + 1;
            }
        }
        return ans;
    }

    private static int calculateWithdrawCount(List<Integer> moneys, int withdrawMoney) {
        int totalMoney = 0, cnt = 0;
        for (int i = 0; i < moneys.size(); i++) {
            if (totalMoney < moneys.get(i)) {
                totalMoney = withdrawMoney;
                cnt++;
            }
            totalMoney -= moneys.get(i);
        }
        return cnt;
    }

}