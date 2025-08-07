class Solution {
    public int solution(String my_string, String is_prefix) {
        int answer = 0;
        if(my_string.startsWith(is_prefix)) {
            return 1;
        }
        else {
            return 0;
        }
    }
}