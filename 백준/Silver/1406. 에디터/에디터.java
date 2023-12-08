import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 1. 초기
        // 커서의 왼쪽 스택 [a b c d|]
        // 커서의 오른쪽 스택 []
        // 2. P x
        // 커서의 왼쪽 스택 [a b c d x|]
        // 커서의 오른쪽 스택 []
        // 3.L
        // 커서의 왼쪽 스택 [a b c d |]
        // 커서의 오른쪽 스택 [x]
        // 4. P y
        // 커서의 왼쪽 스택 [a b c d y| ]
        // 커서의 오른쪽 스택 [x]
        // 5. L
        // 커서의 왼쪽 스택 [a b c d | ] > 순서대로
        // 커서의 오른쪽 스택 [x, y] > 반대로
        // 정답: a b c d y x
        String input = br.readLine();
        // 커서의 왼쪽에 존재하는 문자열
        Stack<String> leftStack = new Stack<>();
        // 커서의 오른쪽에 존재하는 문자열
        Stack<String> rightStack = new Stack<>();

        for (int i = 0; i < input.length(); i++) {
            leftStack.push(String.valueOf(input.charAt(i)));
        }

        int M = Integer.parseInt(br.readLine());
        for (int i = 0; i < M; i++) {
            String[] inputCommand = br.readLine().split(" ");
            if (inputCommand[0].equals("P")) {
                leftStack.push(inputCommand[1]);
            } else if (inputCommand[0].equals("L")) {
                if (!leftStack.isEmpty()) {
                    rightStack.push(leftStack.pop());
                }
            } else if (inputCommand[0].equals("D")) {
                if (!rightStack.isEmpty()) {
                    leftStack.push(rightStack.pop());
                }
            } else {
                if (!leftStack.isEmpty()) {
                    leftStack.pop();
                }
            }
        }
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (String l : leftStack) {
            bw.write(l);
        }
        while(!rightStack.isEmpty()){
            bw.write(rightStack.pop());
        }
        bw.flush();
    }
}