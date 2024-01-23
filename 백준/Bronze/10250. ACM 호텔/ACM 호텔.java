import java.io.*;
import java.util.*;

public class Main {
    private static int T;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // StringTokenizer st;
        T = Integer.parseInt(br.readLine());
        for(int i = 0; i < T; i++){
            StringTokenizer input = new StringTokenizer(br.readLine());
            int H = Integer.parseInt(input.nextToken());
            int W = Integer.parseInt(input.nextToken());
            int N = Integer.parseInt(input.nextToken());
            System.out.println(calculateRoomNumber(H, W, N));
        }

    } 

    private static int calculateRoomNumber(int H, int W, int N){
        // 1순위: 엘리베이터로부터의 거리 
        // 거리1의 모든 방을 채운 후 거리2의 방을 채우고....
        // 높이의 배수인지 확인해야함! / 가 아니라 % 로 해야지 <- 실수
        int XX = (N % H != 0) ? N / H + 1 : N / H;
        // 2순위: 거리 채운 후 층을 채워야함.
        // 10이면 6층 건물에서 4층에 살아야함.  
        int YY = (N % H != 0) ? N % H : H;
        return YY * 100 + XX;
    }
}