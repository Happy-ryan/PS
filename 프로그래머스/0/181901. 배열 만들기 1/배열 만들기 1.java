import java.util.*;

class Solution {
    public int[] solution(int n, int k) {

        List<Integer> list = new ArrayList<>();
        
        for (int num = 1; num <= n; num++) {
            if (num % k == 0) {
                list.add(num);
            }
        }
        
        int[] answer = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }
        
        
        return answer;
    }
}