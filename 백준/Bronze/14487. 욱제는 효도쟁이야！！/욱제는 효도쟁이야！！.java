import java.util.*;

public class Main {

    private static int n;
    private static List<Integer> costs = new ArrayList<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            costs.add(x);
        }

        Collections.sort(costs);

        int sumCost = 0;
        for (int i = 0; i < costs.size() - 1; i++) {
            sumCost += costs.get(i);
        }

        System.out.println(sumCost);

    }

}
