import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 이분탐색 -> 정수 제곱근(logn)
        // int: -21억 ~ 21억 > 넘어가면 long 사용!
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long n = Long.parseLong(br.readLine());
        System.out.println(binarySearch(n));
    }

    private static Long binarySearch(Long number) {
        // 2^63 = (10^3)^6 = 10^18 + @
        long l = -1;
        // q^2 >= number 중 음이 아닌 가장 작은 q
//        long r = (long) Math.pow(10, 10);
        long r = 3037000500L;
        while (true) {
            long m = (l + r) / 2;
            if (r - l <= 1) {
                break;
            }
            // m^2 > number인 상태면 r을 줄여야함.
            // m^2 하면 2^63-1을 거의 넘음. > m^2 지양
            if (m * m >= number) {
                r = m;
            } else {
                l = m;
            }
        }
        // ex) 48의 정답 7 > 이분탐색 l: 6, r: 8, m: 7 > 7^2 은 48보다 크다. r = m
        return r;
    }
}