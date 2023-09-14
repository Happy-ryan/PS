import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<String> row = new ArrayList<String>();
        row.add("+");
        while (true) {
            String s = sc.next();
            if (s.equals("=")) {
                break;
            }
            row.add(s);
        }
        int cnt = 0;
        for (int i = 0; i < row.size(); i += 2) {
            if (row.get(i).equals("+")) {
                cnt += Integer.parseInt(row.get(i + 1));
            } else if (row.get(i).equals("-")) {
                cnt -= Integer.parseInt(row.get(i + 1));
            } else if (row.get(i).equals("*")) {
                cnt *= Integer.parseInt(row.get(i + 1));
            } else {
                cnt /= Integer.parseInt(row.get(i + 1));
            }
        }
        System.out.println(cnt);
    }
}
