class Solution {
    public String solution(String myString, String pat) {
        StringBuilder sb = new StringBuilder();
        
        int x = 0, idx = 0;
        int size = pat.length();
        while (idx < myString.length() - size + 1) {
            if (myString.substring(idx, idx + size).equals(pat)) {
                x = Math.max(x, idx);
            }
            idx++;
        }
        
        System.out.println(x);
        
        for(int i = 0; i < x + size; i++) {
            sb.append(myString.charAt(i));
        }

        
        return sb.toString();
    }
}