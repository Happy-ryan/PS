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
            List<Integer> arr = new ArrayList<>();
            for (int k = 0; k < n; k++) {
                int p = Integer.parseInt(inputPriority.nextToken());
                priorities.add(p);
                documents.add(k);
                arr.add(p);
            }
            System.out.println(printQueue(priorities, documents, arr, m));
        }
    }

    private static int printQueue(Deque<Integer> prioritys,
                                  Deque<Integer> documents,
                                  List<Integer> arr,
                                  int m) {
        List<Integer> answer = new ArrayList<>(prioritys.size());
        Collections.sort(arr, Collections.reverseOrder());
        int idx = 0;
        while (idx < arr.size()) {
            int maxPriority = arr.get(idx); // 시간복잡도 1
            if (maxPriority == prioritys.getFirst()) {
                answer.add(documents.pollFirst());
                prioritys.pollFirst();
                idx++;
            } else {
                prioritys.add(prioritys.pollFirst());
                documents.add(documents.pollFirst());
            }
        }
        return answer.indexOf(m) + 1;
    }
}