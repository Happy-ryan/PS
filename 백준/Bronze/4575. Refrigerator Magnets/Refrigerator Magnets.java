import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            String s = scanner.nextLine();
            if (s.equals("END")) {
                break;
            }
            Map<Character, Integer> map = new HashMap<>();
            boolean flag = true;
            for (char c : s.toCharArray()) {
                if (c != ' ') {
                    map.put(c, map.getOrDefault(c, 0) + 1);
                    if (map.get(c) > 1) {
                        flag = false;
                        break;
                    }
                }
            }
            if (flag) {
                System.out.println(s);
            }
        }
    }
}