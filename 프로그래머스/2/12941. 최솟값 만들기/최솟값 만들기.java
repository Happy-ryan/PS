import java.util.*;

class Solution
{
    public int solution(int []A, int []B)
    {
        int answer = 0;
        // 그리디 & 완탐
        // 가장 작은수 * 가장 큰수
        Arrays.sort(A);
        Arrays.sort(B);

        for (int i = 0; i < A.length; i++) {
            answer += (A[i] * B[A.length - 1 - i]);
        }

        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        System.out.println("Hello Java");

        return answer;
    }
}