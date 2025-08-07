class Solution {
    public String solution(String my_string, int[] index_list) {
        StringBuilder answer = new StringBuilder();
        
        for (int idx : index_list) {
            char txt = my_string.charAt(idx);
            answer.append(txt);
        }
        
        return answer.toString();
    }
}