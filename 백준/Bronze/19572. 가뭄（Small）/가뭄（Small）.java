import java.io.*;
import java.util.*;

class Solution {
    public String solution(int x, int y, int z) {
        StringBuilder sb = new StringBuilder();

        double a = (x + y - z) / 2.0;
        double b = x - a;
        double c = y - a;

        if (a <= 0 || b <= 0 || c <= 0) {
            sb.append("-1\n");
        } else {
            sb.append("1\n");
            sb.append(String.format("%.1f %.1f %.1f\n", a, b, c));  // 소수점 첫째 자리까지 출력
        }

        // 최종 결과 반환
        return sb.toString();
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        int z = Integer.parseInt(st.nextToken());

        // Solution 객체 생성 후 solution 메서드 호출
        Solution sol = new Solution();
        System.out.println(sol.solution(x, y, z));  // 반환된 문자열 출력
    }
}
