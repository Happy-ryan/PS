import java.util.*;
import java.io.*;

public class Main {

    private static int N, M;
    private static int MAX = 50;
    private static char[][] board = new char[MAX][MAX];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        for (int r = 0; r < N; r++){
            String row = br.readLine();
            for (int c = 0; c < M; c++) {
                board[r][c] = row.charAt(c);
            }
        }

        System.out.println(Math.max(countRow(), countCol()));
    }
    private static int countRow() {
        int rowCount = 0;
        for(int r = 0; r < N; r++){
            List<Character> arr = new ArrayList<>();
            for (int c = 0; c < M; c++) {
                arr.add(board[r][c]);
            }
            if (!arr.contains('X')) {
                rowCount++;
            }
        }
        return rowCount;
    }

    private static int countCol() {
        int colCount = 0;
        for (int c = 0; c <M; c++) {
            List<Character> arr = new ArrayList<>();
            for(int r = 0; r < N; r++) {
                arr.add(board[r][c]);
            }
            if( !arr.contains('X')){
                colCount++;
            };
        }
        return colCount;
    }
}
