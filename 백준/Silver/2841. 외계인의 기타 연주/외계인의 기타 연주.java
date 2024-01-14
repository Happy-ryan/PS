import java.io.*;
import java.util.*;

public class Main {

    public static int n, m; 

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer inputNM = new StringTokenizer(br.readLine());

        n = Integer.parseInt(inputNM.nextToken());
        m = Integer.parseInt(inputNM.nextToken());

        Map<Integer, List<Integer>> guitarMelody = new HashMap<>();

        for (int i = 0; i < n; i++) {
            StringTokenizer row = new StringTokenizer(br.readLine());

            int stringNumber = Integer.parseInt(row.nextToken());
            int platNumber = Integer.parseInt(row.nextToken());

            List<Integer> platList = guitarMelody.get(stringNumber);
            if (platList == null) {
                platList = new ArrayList<>();
                guitarMelody.put(stringNumber, platList);
            }
            platList.add(platNumber);
        }

        int ans = 0;
        for (List<Integer> plats : guitarMelody.values()) {
            ans += countFingerNumber(plats);
        }

        System.out.println(ans);

    }

    public static int countFingerNumber(List<Integer> plats) {
        Deque<Integer> stack = new ArrayDeque<>();  
        int cnt = 0;

        for (int plat : plats) {
            while (!stack.isEmpty() && stack.peek() > plat) {
                stack.pop();
                cnt++;
            }
            if (stack.isEmpty() || stack.peek() < plat) {
                stack.push(plat);
                cnt++;
            }
        }
        return cnt;
    }
}