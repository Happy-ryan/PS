import java.util.*;

public class Main {

    private static int n, s;

    private static List<Integer> numbers = new ArrayList<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        s = sc.nextInt();


        for (int i = 0; i < n; i++) {
            int num = sc.nextInt();
            numbers.add(num);
        }

        int cnt = DFS(0, 0);

        if (s == 0) {
            cnt--;
        }
        System.out.println(cnt);

    }

    private static int DFS(int level, int sum) {
        int cnt = 0;
        if (level == n) {
            if (sum == s) {
                return 1;
            }
            return 0;
        }

        cnt += DFS(level + 1, sum + numbers.get(level));
        cnt += DFS(level + 1, sum);

        return  cnt;
    }
}