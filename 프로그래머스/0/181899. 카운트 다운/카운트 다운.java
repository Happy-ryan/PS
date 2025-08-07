class Solution {
    public int[] solution(int start_num, int end_num) {
        int size = start_num - end_num + 1;
        int[] answer = new int[size];
        int idx = 0;
        for (int i = start_num; end_num <= i; i--) {
            // System.out.println(i);
            answer[idx++] = i;
        }
        return answer;
    }
}