import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String s1 = sc.nextLine();
        String s2 = sc.nextLine();
        String ans = "";

        for (int i = 0; i < s1.length(); i++) {
            char x = s1.charAt(i);
            if (x == ' ') {
                ans += ' ';
            } else {
                int orgin = (int) x;
                int key = (int) s2.charAt(i % s2.length()) - (int) 'a' + 1;
                int en = orgin - key + (orgin - key < 'a' ? 26 : 0);
                ans += (char) en;
            }
        }
        System.out.println(ans);
    }
}