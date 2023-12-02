import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        // 중복 허용 x
        List<String> arr = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            if (!arr.contains(s)) {
                arr.add(s);
            }
        }
        // 2. 사전순 배열
        Collections.sort(arr);
        // 1. 길이 짧은 것부터 - 올림차순
        Collections.sort(arr, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                if (o1.length() < o2.length()) {
                    return -1;
                } else if (o1.length() > o2.length()) {
                    return 1;
                }
                return 0;
            }
        });
        for (String str : arr) {
            System.out.println(str);
        }
    }
}