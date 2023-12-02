import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            int number = Integer.parseInt(br.readLine());
            System.out.println(check(number));
        }
    }

    private static int check(int number) {
        int ans = 0;
        for (int m = 2; m < 65; m++) {
            String res = convert(number, m);
            if (isPalindrome(res)) {
                ans = 1;
            }
        }
        return ans;
    }

    // 회문 확인하기
    private static boolean isPalindrome(String str) {
        for (int idx = 0; idx < str.length() / 2; idx++) {
            if (str.charAt(idx) != str.charAt(str.length() - idx - 1)) {
                return false;
            }
        }
        return true;
    }

    // 10진법 number -> m진법으로 변경
    private static String convert(int number, int m) {
        // reverse를 사용하기 위해서 StringBuilder 사용!
        StringBuilder res = new StringBuilder();
        // 0 - 9 : 10
        // a - z : 26
        // A - z : 26
        // @, * : 2
        // 64
        String conv = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@*";

        if (number == 0) {
            res.append("0");
            return "0";
        }

        while (number > 0) {
            // String.valueOf: object -> String
            String k = String.valueOf(conv.charAt(number % m));
            res.append(k);
            number /= m;
        }
        // StringBuilder -> String
        return res.reverse().toString();
    }
}