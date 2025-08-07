class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        String str = "";
        StringBuilder sb = new StringBuilder ();
        for (char x : myString.toCharArray()) {
            if (x == 'A') {
                str += 'B';
                sb.append('B');
            }
            else {
                str += 'A';
                sb.append('A');
            }
        }
        return sb.toString().contains(pat) ? 1 : 0;
    }
}