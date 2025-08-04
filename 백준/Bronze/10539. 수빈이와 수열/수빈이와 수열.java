import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        List<Integer> arr = new ArrayList<>(n);
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr.add(Integer.parseInt(st.nextToken()));
        }

        List<Integer> brr = new ArrayList<>(n);


        int val = 0;
        int cnt = 0;

        for(int k = 0; k < n; k++) {
            val = arr.get(k);
            cnt++;
            brr.add(val * cnt);
        }

        for (int k = 0; k < n; k++) {
            if (k == 0) {
                System.out.print(brr.get(k) + " ");
            } else {
                System.out.print(brr.get(k) - brr.get(k - 1) + " ");
            }
        }

    }
}