import java.util.*;

public class Main {

    private static  int n, m;
    private static  List<Integer> nums = new ArrayList<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        m = sc.nextInt();
        for (int i = 0; i < n; i++) {
            int num = sc.nextInt();
            nums.add(num);
        }

        long mulVal = 1;
        for (int num : nums) {
            mulVal *= (num % m);
            mulVal %= m;
        }

        System.out.print(mulVal);
    }
}