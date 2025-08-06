import java.util.*;

public class Main {
    static int n;
    static long[] A, B; // Ai, Bi 범위가 최대 10^18이므로 long 사용

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        A = new long[n];
        B = new long[n];

        for (int i = 0; i < n; i++) {
            A[i] = sc.nextLong();
        }
        for (int i = 0; i < n; i++) {
            B[i] = sc.nextLong();
        }

        solution();
    }

    static void solution() {
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < n; i++) {
            int idx = binary(A[i]);
            sb.append(idx - i).append(" ");
        }

        System.out.println(sb.toString().trim());
    }

    // B 배열에서 target 이하의 값 중 가장 오른쪽 인덱스를 찾는 이진 탐색
    static int binary(long target) {
        int l = 0, r = n - 1;
        while (l <= r) {
            int m = (l + r) / 2;
            if (target < B[m]) {
                r = m - 1;
            } else {
                l = m + 1;
            }
        }
        return r; // target 이하의 값의 마지막 인덱스
    }
}
