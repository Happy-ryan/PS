import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {

    public static StringBuilder sb = new StringBuilder();

    public static void hanoi(int n, int s, int e){
        if (n == 1){
            sb.append(s + " " + e + "\n");
            return;
        }
        hanoi(n - 1, s, 6 - s - e);
        sb.append(s + " " + e + "\n");
        hanoi(n - 1, 6 - s - e, e);
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        // 하노이탑퍼즐의 최소 이동 회수 : 2^n - 1
        // java에서는 2**n 불가능
        // Math.pow(2, n) 사용 후 정수형으로 변형!
        sb.append((int) (Math.pow(2, n) - 1)).append('\n');
        hanoi(n, 1, 3);
        System.out.println(sb);
    }
}