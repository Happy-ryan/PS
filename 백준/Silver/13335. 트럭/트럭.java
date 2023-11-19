import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt((st.nextToken()));
        int w = Integer.parseInt((st.nextToken()));
        int L = Integer.parseInt((st.nextToken()));

        Queue<Integer> trucks = new ArrayDeque<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            trucks.add(Integer.parseInt(st.nextToken()));
        }

        Queue<Integer> q = new ArrayDeque<>();
        int t = 0;

        while (!trucks.isEmpty()) {
            int truck = trucks.peek();

            if (q.size() == w) {
                q.poll();
            }

            if (calculateTotalWeight(q) + truck <= L) {
                truck = trucks.poll();
                q.add(truck);
            }
            // 다리 위에 올라갈 수 없으면 0을 추가!
            else {
                q.add(0);
            }
            t++;
        }
        // 마지막 트럭이 다리 위에 올라오는 순간 trucks는 Empty가 된다. 그래서 while문이 더 이상 진행하지 않는다.
        // 마지막 트럭도 w길이를 가진 다리를 이동해야하므로 t에 w를 더해주면 마자믹 트럭까지 다리를 전부 이동했을 때의 시간이 나오게 된다.
        System.out.println(t + w);
    }
    private static int calculateTotalWeight(Queue<Integer> q) {
        int totalWeight = 0;
        for (int value : q) {
            totalWeight += value;
        }
        return totalWeight;
    }
}