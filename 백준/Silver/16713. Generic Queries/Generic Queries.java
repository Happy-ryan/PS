import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static List<Integer> arr;
    private static List<Integer> prefixSum;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        arr = new ArrayList<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr.add(Integer.parseInt(st.nextToken()));
        }

        prefixSum = new ArrayList<>();
        prefixSum.add(0);
        // xor의 누적합이용
        // 0을 맨 앞에 넣어서 1base로 전환
        // idx = 1; (1, 1)의 xor 연산 a
        // idx = 2; (1, 2)의 xor 연산 a^b
        // idx = 3; (1, 3)의 xor 연산 a^b^c
        // (2, 3)의 xor연산 = b^c -> (1, 3)의 xor연산 ^ (1, 1)의 연산 = (a^b^c) ^ (a) = 0^b^c = b^c
        for (int i = 0; i < n; i++) {
            prefixSum.add(arr.get(i) ^ prefixSum.get(i));
        }
//        System.out.println(prefixSum);

        int answer = 0;
        for (int t = 0; t < q; t++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            answer ^= (prefixSum.get(e) ^ prefixSum.get(s - 1));
        }
        System.out.println(answer);
    }

}