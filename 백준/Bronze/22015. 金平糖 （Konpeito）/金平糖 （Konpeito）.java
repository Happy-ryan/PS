import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] arr = new int[3];
        for (int i = 0; i < 3; i++) {
            arr[i] = scanner.nextInt();
        }
        int res = max(arr) * 3 - sum(arr);
        System.out.println(res);
    }

    public static int max(int[] arr) {
        int maxVal = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > maxVal) {
                maxVal = arr[i];
            }
        }
        return maxVal;
    }

    public static int sum(int[] arr) {
        int sumVal = 0;
        for (int i = 0; i < arr.length; i++) {
            sumVal += arr[i];
        }
        return sumVal;
    }
}