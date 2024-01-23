import java.io.*;
import java.util.*;

public class Main {
    private static String A, B;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer input = new StringTokenizer(br.readLine());

        A = input.nextToken();
        B  = input.nextToken();
        // String에도 포함여부를 판단하는 contains 함수 존재 
        // 포함되면 아무거나 붙일 수 있으므로 0
        if(B.contains(A)){
            System.out.println(0);
        }
        else{
            if(A.length() == B.length()){
                System.out.println(sameLength(A, B));
            }
            else{
                System.out.println(differentLength(A, B));
            }
        }

    } 

    private static int sameLength(String A, String B){
        int cnt = 0;
        for(int i = 0; i < A.length() ; i ++){
            // char는 비교할 때 != 로 해도 되구나
            if(A.charAt(i) != B.charAt(i)){
                cnt++;
            }
        }
        return cnt;
    }

    private static int differentLength(String A, String B){
    //   B의 맨 앞에서부터 움직여서 비교할 것
    //  topcoder - 8
    //  koder@@@ - 5
    //  @koder@@
    //  @@koder@
    //  @@@koder
    //  @는 내가 원하는대로 넣을 수 있다. 
    //  그러므로 지금 있는 문자가 많이 겹쳐야한다.
    //  시간복잡도: O(N^2)
        int minCnt = B.length();
        for(int i = 0; i <= B.length() - A.length(); i++){
            int cnt = 0;
            // j의 범위는 j + i + 0, ... j + i + A.length() - 1
            // j의 범위 체크에서 틀림..i를 까먹으면 안 된다!
            for(int j = i; j < i + A.length(); j++){
                if(A.charAt(j - i) != B.charAt(j)){
                    cnt++;
                }
            }
            minCnt = Math.min(minCnt, cnt);
        }
        return minCnt;
    }
}
