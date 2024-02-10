import java.util.*;

public class Main {
    private static int n;
    private static Set<Integer> setNums = new HashSet<>();
    private static List<Integer> sortedNums;
    
    private static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        n = sc.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i <n; i++) {
            int x = sc.nextInt();
            setNums.add(x);
            nums[i] = x;
        }

        sortedNums = new ArrayList<>(setNums);
        Collections.sort(sortedNums);

        for (int i = 0; i < n; i++) {
            sb.append(binarySearch(nums[i]) + " ");
        }
        
        System.out.print(sb);

    }

    private static int binarySearch(int target) {
        int l = 0;
        int r = sortedNums.size() - 1;
        int ans = -1;
        while (l <= r) {
            int mid = (l + r) / 2;
            //  target보다 크지만 가장 작은 값..
            if (sortedNums.get(mid) >= target) {
                ans = mid;
                r = mid - 1;
            }
            else {
                l = mid + 1;
            }
        }
        return ans;
    }
}