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
        
        int last_idx = myString.lastIndexOf(pat);
        
        System.out.println(last_idx);
        
        for(int i = 0; i < last_idx + size; i++) {
            sb.append(myString.charAt(i));
        }

        
        return sb.toString();
    }
}