import java.util.*;

class Solution {
    public int[] solution(int n) {
        int[] answer;
        int tmp = n;
        
        List<Integer> list = new ArrayList<>();
        list.add(tmp);
        
        while (tmp != 1) {
            
            if (tmp % 2 == 0){
                tmp /= 2;
            }
            else {
                tmp = tmp * 3 + 1;
            }
            list.add(tmp);
        }
        
        int size = list.size();
        answer = new int[size];
        
        for (int i = 0; i < size; i++) {
            answer[i] = list.get(i);
        }
        return answer;
    }
}