import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        String s = sc.next();

        if (count(s, '2') > count(s, 'e')) {
            System.out.println('2');
        } else if (count(s, '2') < count(s, 'e')) {
            System.out.println('e');
        } else {
            System.out.println("yee");
        }
    }

    public static int count(String str, char target) {
        int count = 0;
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == target) {
                count++;
            }
        }
        return count;
    }
}
