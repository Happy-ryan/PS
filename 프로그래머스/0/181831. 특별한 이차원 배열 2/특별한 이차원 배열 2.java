class Solution {
    public int solution(int[][] arr) {
        int answer = 0;
        boolean flag = true;
        
        int N = arr.length;
        int M = arr[0].length;
        
        
        for(int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (arr[i][j] != arr[j][i]) {
                    flag = false;
                }
            }
        }
        return flag ? 1 : 0;
    }
}