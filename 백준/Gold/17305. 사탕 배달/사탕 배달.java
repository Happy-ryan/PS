import java.util.*;

public class Main {
    public static int n, w;

    public static List<Integer> threeWeightCandies = new ArrayList<>();
    public static List<Integer> fiveWeightCandies = new ArrayList<>();

    public static void main(String[] args) {
        // 입력
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        w = sc.nextInt();

        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            if (x == 3){
                threeWeightCandies.add(y);
            }
            else{
                fiveWeightCandies.add(y);
            }
        }
        // 내림차순 정렬 - 당도가 높은 것부터!
        Collections.sort(threeWeightCandies, Collections.reverseOrder());
        Collections.sort(fiveWeightCandies, Collections.reverseOrder());
        // 무게3의 사탕으로만 이루어진 최대 당도
        long totalSweet = 0;
        List<Integer> threeCandies = new ArrayList<>();
        for(int sweet : threeWeightCandies){
            if (0 <= w - 3){
                totalSweet += sweet;
                threeCandies.add(sweet);
                w -= 3;
            }
        }
        // 남은 무게 고려 & 무게3으로만 이루어진 threeCandies를 무게5 사탕으로 변경하면서 최대 당도 찾아내기
        int idx = 0;
        long maxTotalSweet = totalSweet;
        int k = threeCandies.size();
        for (int i = 0; i <= k; i++) {
            // 남은 무게가 5이상인 경우
            while (w >= 5 && idx < fiveWeightCandies.size()){
                w -= 5;
                totalSweet += fiveWeightCandies.get(idx);
                maxTotalSweet = Math.max(maxTotalSweet, totalSweet);
                idx++;
            }
            // 당도가 가장 작은 것부터 제거
            if (threeCandies.size() != 0) {
                totalSweet -= threeCandies.get(threeCandies.size() - 1);
                threeCandies.remove(threeCandies.size() - 1);
                w += 3;
            }
        }
        System.out.println(maxTotalSweet);
    }
}