import java.util.*;

public class Main {

    public static void main(String[] args) {
        // 입력
        Scanner sc = new Scanner(System.in);
        // int(32bit): -2^31 ~ 2^31 - 1
        // long(64bit): -2^63 ~ 2^63 - 1 
        long a = sc.nextLong();
        long b = sc.nextLong();

        System.out.println(a + b);
    }
}