import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] str = scanner.nextLine().split(" ");
        Map<String, Integer> dic = new HashMap<>();
        boolean flag = false;

        for (String word : str) {
            dic.put(word, dic.getOrDefault(word, 0) + 1);
        }

        for (int value : dic.values()) {
            if (value >= 2) {
                flag = true;
                break;
            }
        }

        System.out.println(flag ? "no" : "yes");
        scanner.close();
    }
}