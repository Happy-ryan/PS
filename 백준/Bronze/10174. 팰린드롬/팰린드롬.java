import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.nextLine()); 

        for (int i = 0; i < n; i++) {
            //  next()와 nextLine() 차이 알아보기!
            String s = sc.nextLine(); // 공백 입력 받을 때 주의!
            if (isPalindrome(s)) {
                System.out.println("Yes");
            } else {
                System.out.println("No");
            }
        }
    }

    // 팰린드롬 여부를 확인하는 함수
    public static boolean isPalindrome(String s) {
        // 소문자로 변경하는 자바 메서드
        s = s.toLowerCase();
        for (int i = 0; i < s.length() / 2; i++) {
            if (s.charAt(i) != s.charAt(s.length() - i - 1)) {
                return false;
            }
        }
        return true;
    }
}