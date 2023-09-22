import java.io.*;
import java.util.*;

public class Main {
    public static final int MAX_K = 100;
    //
    public static String[] ts = new String[5];
    public static int[][] cmds = new int[MAX_K][2];
    public static int[] check = new int[5];
    // 반시계 회전
    public static String ccw(String t) {
        char temp = t.charAt(0);
        StringBuilder rotated = new StringBuilder(t.substring(1));
        rotated.append(temp);
        return rotated.toString();
    }
    // 시계 회전
    public static String cw(String t) {
        char temp = t.charAt(t.length() - 1);
        StringBuilder rotated = new StringBuilder(temp + t.substring(0, t.length() - 1));
        return rotated.toString();
    }
    // 톱니번호에 따른 회전
    public static String t1Simulate(int cmd){
        check[1] = 1;

        if(check[2] == 0 && ts[1].charAt(2) != ts[2].charAt(6)){
            ts[2] = t2Simulate(-cmd);
        }

        if (cmd == 1) {
            ts[1] = cw(ts[1]);
        } else {
            ts[1] = ccw(ts[1]);
        }
        return ts[1];
    }
    public static String t2Simulate(int cmd){
        check[2] = 1;

        if(check[3] == 0 && ts[2].charAt(2) != ts[3].charAt(6)){
            ts[3] = t3Simulate(-cmd);
        }
        if(check[1] == 0 && ts[2].charAt(6) != ts[1].charAt(2)){
            ts[1] = t1Simulate(-cmd);
        }
        if (cmd == 1) {
            ts[2] = cw(ts[2]);
        } else {
            ts[2] = ccw(ts[2]);
        }  
        return ts[2];
    }
    public static String t3Simulate(int cmd){
        check[3] = 1;

        if(check[2] == 0 && ts[3].charAt(6) != ts[2].charAt(2)){
            ts[2] = t2Simulate(-cmd);
        }
        if(check[4] == 0 && ts[3].charAt(2) != ts[4].charAt(6)){
            ts[4] = t4Simulate(-cmd);
        }
        if (cmd == 1) {
            ts[3] = cw(ts[3]);
        } else {
            ts[3] = ccw(ts[3]);
        }
        return ts[3];
    }
    public static String t4Simulate(int cmd){
        check[4] = 1;

        if(check[3] == 0 && ts[4].charAt(6) != ts[3].charAt(2)){
            ts[3] = t3Simulate(-cmd);
        }

        if (cmd == 1) {
            ts[4] = cw(ts[4]);
        } else {
            ts[4] = ccw(ts[4]);
        }
        return ts[4];
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 1; i <= 4; i++) { // 톱니바퀴 번호 1부터 4까지 사용
            StringTokenizer st = new StringTokenizer(br.readLine());
            ts[i] = st.nextToken();
        }
        StringTokenizer st = new StringTokenizer(br.readLine());
        int k = Integer.parseInt(st.nextToken()); 
        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            cmds[i][0] = Integer.parseInt(st.nextToken()); // cmds[i][0]에 저장
            cmds[i][1] = Integer.parseInt(st.nextToken()); // cmds[i][1]에 저장
        }
    
        for(int i = 0; i < k; i++){
            check = new int[]{0, 0, 0, 0, 0};
            int num = cmds[i][0];
            int cmd = cmds[i][1];
            if (num == 1)
                t1Simulate(cmd);
            else if (num == 2)
                t2Simulate(cmd);
            else if (num == 3)
                t3Simulate(cmd);
            else
                t4Simulate(cmd);
        }
        int sum_val = 0;
        for(int i = 1; i < 5; i++){
            if (ts[i].charAt(0) == '1'){
                 sum_val += Math.pow(2, i - 1);
            }
        }
        System.out.print(sum_val);
    }
}