import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String s1 = sc.nextLine();
        String s2 = sc.nextLine();
        String ans = "";

        for (int idx = 0; idx < s1.length(); idx++) {
            char x = s1.charAt(idx);
            // 공백 유지
            if (x == ' ') {
                ans += ' ';
            } 
            // 공백 제외 평문의 아스키코드
            else {
                int orgin = (int) s1.charAt(idx);
                // 암호화 키의 알파벳 순서 -> 암호화 키 안에서 돌기 때문에 모듈러 연산 도입! -> 나머지
                int p = idx % s2.length();
                int key = (int) s2.charAt(p) - (int) 'a' + 1;
                // 암호화 아스키 코드
                int en = orgin - key;
                // en이 a보다 작아질 경우 z로 되돌아가 값 출력
                if (97 <= en && en <= 122) {
                    ans += (char) en;
                } else {
                    en += 26;
                    ans += (char) en;
                }
            }
        }
        System.out.println(ans);
    }
}