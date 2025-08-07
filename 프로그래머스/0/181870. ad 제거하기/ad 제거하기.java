import java.util.*;

class Solution {
    public String[] solution(String[] strArr) {
        String[] answer;
        
        List<String> list = new ArrayList<>();
        for(String str : strArr) {
            if(!str.contains("ad")) {
                list.add(str);
            }
        }
        answer = new String[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }
        return answer;
    }
}