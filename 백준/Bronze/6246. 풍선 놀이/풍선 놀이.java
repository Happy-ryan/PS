import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int q = scanner.nextInt();
        int[] arr = new int[n + 1];
        
        for (int i = 0; i < q; i++) {
            int L = scanner.nextInt();
            int I = scanner.nextInt();
            
            for (int j = L; j <= n; j += I) {
                arr[j] = 1;
            }
        }
        
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            sum += arr[i];
        }
        
        System.out.println(n - sum);
    }
}