import java.io.*;
import java.util.*;

public class Main {
    private static int L, C;
    private static List<String> alpabets;

    private static List<String> ans;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer input = new StringTokenizer(br.readLine());

        L = Integer.parseInt(input.nextToken());
        C = Integer.parseInt(input.nextToken());

        alpabets = new ArrayList<>(C);
        StringTokenizer inputAlpabet = new StringTokenizer(br.readLine());
        for(int i = 0; i < C; i++){
            alpabets.add(inputAlpabet.nextToken());
        }
        // 증가하는 순이므로 정렬 필요함(자바 정렬 - Collections.sort(배열)
        Collections.sort(alpabets);

        ans = new ArrayList<>();
        dfs(0, 0);
    } 

    private static void dfs(int level, int idx){
        if (level == L){
            // 모음 1개이상, 자음 2개이상
            if (check(ans)){
                prettyPrint(ans);
            }
            return;
        }
        for (int i = idx; i < C; i++) {
        ans.add(alpabets.get(i));
        dfs(level + 1, i + 1);
        ans.remove(ans.size() - 1);
        }
    
    }

        private static boolean check(List<String> ans){
        int 모음 = 0;
        int 자음 = 0;
        for(String string : ans){
            if ("aeiou".contains(string)){
                모음++;
            }
            else{
                자음++;
            }
        }

        if (모음 >=1 && 자음>= 2){
            return true;
        }
        return false;
    } 

    private static void prettyPrint(List<String> ans){
        StringBuilder sb = new StringBuilder();
        for(String string : ans){
            sb.append(string);
        }
        System.out.println(sb.toString());
    }
}