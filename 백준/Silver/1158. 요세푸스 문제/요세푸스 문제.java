import java.util.*;

public class Main {
    public static int n, k;

    public static Deque<Integer> dq = new ArrayDeque<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        k = sc.nextInt();

        for(int i = 1; i <= n; i++) {
            dq.add(i);
        }


        List<Integer> ans = new ArrayList<>();
        while (dq.size()!= 0) {
            rotate();
            ans.add(dq.removeFirst());
        }

        prettyPrint(ans);
    }

    public static void rotate() {
        // k번째를 뽑기 위해서 k - 1 번 앞에서 뒤로 보내고 k번째 숫자 뽑아내기
        for (int i = 0; i < k - 1; i++) {
            int tmp = dq.removeFirst();
            dq.add(tmp);
        }
    }

    public static void prettyPrint(List<Integer> ans) {
        System.out.print("<");
        for (int i = 0; i < n; i++) {
            if (i == n - 1) {
                System.out.print(ans.get(i) + ">");
                break;
            }
            System.out.print(ans.get(i) + ", ");
        }
    }
}