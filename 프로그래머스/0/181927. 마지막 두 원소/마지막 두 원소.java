class Solution {
    public int[] solution(int[] num_list) {
        int size = num_list.length;
        
        int[] answer = new int[size + 1];
        
        // 삼항연산자
        //(조건문) ? (참) : (거짓)
        for (int i = 0; i < size; i++) {
            if(i == size - 1) {
                answer[size] =  (num_list[i] > num_list[i - 1]) ? num_list[i] - num_list[i - 1] : num_list[i] * 2;
            }
            answer[i] = num_list[i];
        }
        
        return answer;
    }
}