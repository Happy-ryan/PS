import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        HashMap<String, Integer> hsmap = new HashMap<>();
        for (int i = 0; i < N; i++) {
            String input = br.readLine();
            hsmap.put(input, 0);
        }
        for (int i = 0; i < M; i++) {
            String s = br.readLine();
            if(hsmap.containsKey(s)){
                hsmap.put(s, hsmap.get(s) + 1);
            }
        }
        int answer = 0;
        for(int count : hsmap.values()){
            answer += count;
        }
        System.out.println(answer);
    }
}
