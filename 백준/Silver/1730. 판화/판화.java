import java.util.*;

public class Main {

    private static int n;

    private static char[][] upDownBoard;
    private static char[][] leftRightBoard;
    private static char[][] finalBoard;

    public static void main(String[] args) {
        Map<Character, int[]> dir = new HashMap<>();
        dir.put('D', new int[]{1, 0});
        dir.put('U', new int[]{-1, 0});
        dir.put('R', new int[]{0, 1});
        dir.put('L', new int[]{0, -1});

        Scanner sc = new Scanner(System.in);
        
        // Read the size of the board
        n = sc.nextInt();
        sc.nextLine(); // Consume newline character after reading integer
        
        // Read the commands as a string
        String cmds = sc.nextLine();
        
        upDownBoard = new char[n][n];
        leftRightBoard = new char[n][n];

        int cr = 0;
        int cc = 0;

        for (int i = 0; i < cmds.length(); i++) {
            char cmd = cmds.charAt(i);
            int[] directionValues = dir.get(cmd);

            int nr = cr + directionValues[0];
            int nc = cc + directionValues[1];

            if (inRange(nr, nc)) {
                if (cmd == 'D' || cmd == 'U') {
                    upDownBoard[nr][nc] = cmd;
                    upDownBoard[cr][cc] = cmd;
                } else if (cmd == 'R' || cmd == 'L') {
                    leftRightBoard[nr][nc] = cmd;
                    leftRightBoard[cr][cc] = cmd;
                }
                cr = nr;
                cc = nc;
            }
        }

        finalBoard = new char[n][n];
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                if (upDownBoard[r][c] == 0 && leftRightBoard[r][c] == 0) {
                    finalBoard[r][c] = '.';
                } else if (upDownBoard[r][c] != 0 && leftRightBoard[r][c] != 0) {
                    finalBoard[r][c] = '+';
                } else if (upDownBoard[r][c] != 0 && leftRightBoard[r][c] == 0) {
                    finalBoard[r][c] = '|';
                } else if (upDownBoard[r][c] == 0 && leftRightBoard[r][c] != 0) {
                    finalBoard[r][c] = '-';
                }
            }
        }

        // Print the final board
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                System.out.print(finalBoard[r][c]);
            }
            System.out.println();
        }

        // Close the scanner
        sc.close();
    }

    private static boolean inRange(int r, int c) {
        return 0 <= r && r < n && 0 <= c && c < n;
    }
}