import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int ans = 100000000;

        for(int i=0; i<n; i++){
            int a = sc.nextInt();
            int b = sc.nextInt();
            ans = Math.min(ans, b/a);
        }
        System.out.println(ans);
    }
} 