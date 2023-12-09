import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            StringTokenizer inputNM = new StringTokenizer(br.readLine());

            int n = Integer.parseInt(inputNM.nextToken());
            int m = Integer.parseInt(inputNM.nextToken());

            StringTokenizer inputPriority = new StringTokenizer(br.readLine());

            Deque<Integer> priorities = new ArrayDeque<>(n);
            Deque<Integer> documents = new ArrayDeque<>(n);
            for (int k = 0; k < n; k++) {
                priorities.add(Integer.parseInt(inputPriority.nextToken()));
                documents.add(k);
            }
            System.out.println(printQueue(priorities, documents, m));
        }
    }

    private static int printQueue(Deque<Integer> prioritys, Deque<Integer> documents, int m) {
        List<Integer> answer = new ArrayList<>(prioritys.size());
        while (!prioritys.isEmpty()) {
            int maxPriority = maxPriority(prioritys);
            if (maxPriority == prioritys.getFirst()) {
                answer.add(documents.pollFirst());
                prioritys.pollFirst();
            } else {
                prioritys.add(prioritys.pollFirst());
                documents.add(documents.pollFirst());
            }
        }
        return answer.indexOf(m) + 1;
    }

    private static int maxPriority(Deque<Integer> prioritys) {
        int res = 0;
        for (int pri : prioritys) {
            res = Math.max(res, pri);
        }
        return res;
    }
}