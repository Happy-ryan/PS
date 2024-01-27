import java.util.*;

public class Main {

    private static int n, s, cnt;

    private static List<Integer> numbers = new ArrayList<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        s = sc.nextInt();

        cnt = 0;

        for (int i = 0; i < n; i++) {
            int num = sc.nextInt();
            numbers.add(num);
        }

        DFS(0, 0);

        if (s == 0) {
            cnt--;
        }
        System.out.println(cnt);

    }

    private static void DFS(int level, int sum) {
        if (level == n) {
            if (sum == s) {
                cnt++;
            }
            return;
        }

        DFS(level + 1, sum + numbers.get(level));
        DFS(level + 1, sum);
    }
}