import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n ;
        n = sc.nextInt();
        for(int i = 0; i < n; i++){

            int sum = 0;
            double avg, total = 0.0;

            int num = sc.nextInt();
            for(int j = 0; j < num; j++){
                int obj = sc.nextInt();
                double score = sc.nextDouble();
                sum += obj;
                total += obj * score; 
            }
            avg = (double) total / sum;
            System.out.printf("%d %.1f\n", sum, avg);
        }
    }
}