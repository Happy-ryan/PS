class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        String str = "";
        for (char x : myString.toCharArray()) {
            if (x == 'A') {
                str += 'B';
            }
            else {
                str += 'A';
            }
        }
        if (str.contains(pat)) {
            return 1;
        }
        return 0;
    }
}