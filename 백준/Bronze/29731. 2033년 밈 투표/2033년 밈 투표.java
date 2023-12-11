import java.io.*;
import java.util.*;

public class Main {
    private static HashSet<String> hs;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        hs = new HashSet<>();
        hs.add("Never gonna give you up");
        hs.add("Never gonna let you down");
        hs.add("Never gonna run around and desert you");
        hs.add("Never gonna make you cry");
        hs.add("Never gonna say goodbye");
        hs.add("Never gonna tell a lie and hurt you");
        hs.add("Never gonna stop");

        String answer = "No";
        for (int i = 0; i < n; i++) {
            String string = br.readLine();
            if (!hs.contains(string)) {
                answer = "Yes";
                break;
            }
        }
        System.out.println(answer);
    }
}