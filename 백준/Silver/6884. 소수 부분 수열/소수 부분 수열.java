import java.io.*;
import java.util.*;

class Solution {
    public static String solution(int[] nums) {
        String answer = "";

        int size = nums[0];
        int[] psum = new int[size + 1];
        for (int i = 0; i < size; i++) {
            psum[i + 1] = psum[i] + nums[i + 1]; // nums가 1base
        }

//        for(int p : psum) {
//            System.out.println(p);
//        }
//        System.out.println("-");

        int minLength = Integer.MAX_VALUE;
        int minStart = -1;

        // 길이는 최소 2
        for (int w = 2; w < size + 1; w++) {
            boolean found = false;
            for (int i = 0; i < size - w + 1; i++) {
                int val = psum[i + w] - psum[i];
                if (isPrime(val) == 1) {
                    minLength = w;
                    minStart = i;
                    found = true;
                    break;
                }
            }
            if (found) {
                break;
            }
        }

//        System.out.println(minLength);
//        System.out.println(minStart);

        if (minLength == Integer.MAX_VALUE) {
            return "This sequence is anti-primed.";
        }

        StringBuilder sb = new StringBuilder();
        sb.append("Shortest primed subsequence is length ");
        sb.append(minLength).append(": ");

        for (int i = minStart; i < minStart + minLength; i++) {
            sb.append(nums[i + 1]);
            sb.append(" ");
        }

        return sb.toString();
    }

    public static int isPrime(int n) {
        // 0, 1, 2, 짝수 판단
        if (n < 2) {
            return 0;
        }
        if (n == 2) {
            return 1;
        }
        if (n % 2 == 0) {
            return 0;
        }
        // 홀수 판단
        int i = 3;
        while (i * i <= n) {
            if (n % i == 0) {
                return 0;
            }
            i += 2;
        }
        return 1;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        for (int tc = 0; tc < t; tc++) {
            String[] input = br.readLine().split(" ");
            int[] nums = new int[input.length];

            for (int i = 0; i < input.length; i++) {
                nums[i] = Integer.parseInt(input[i]);
            }

            System.out.println(Solution.solution(nums));
        }

        br.close();
    }
}