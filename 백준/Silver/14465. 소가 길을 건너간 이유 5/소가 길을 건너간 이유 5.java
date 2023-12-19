import java.io.*;
import java.util.*;

public class Main {
    private static int N, K, B;
    private static List<Integer> nums;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer input = new StringTokenizer(br.readLine());
        N = Integer.parseInt(input.nextToken());
        K = Integer.parseInt(input.nextToken());
        B = Integer.parseInt(input.nextToken());

        nums = new ArrayList<>();
        for(int i = 0; i <= N; i++){
            nums.add(i);
        }
        List<Integer> broken = new ArrayList<>();
        for(int i = 0; i < B ; i++){
            broken.add(Integer.parseInt(br.readLine()));
        }

        System.out.println(f(broken));
    }

    private static int f(List<Integer> broken){
        int ans = 100001;
        int cnt = 0;
        int l = 1, r = l + K -1;
        for(int i = l; i <= r; i++){
            if(broken.contains(i)){
                cnt++;
            }
        }
        while(r < N){
            if(broken.contains(nums.get(l))){
                cnt--;
            }
            l++;
            r++;
            if(broken.contains(nums.get(r))){
                cnt++;
            }
            ans = Math.min(ans, cnt);
        }
        return ans;
    }

}