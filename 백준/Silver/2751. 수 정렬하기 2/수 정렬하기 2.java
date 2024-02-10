import java.util.*;

public class Main {

    private static int n;
    private static List<Integer> nums = new ArrayList<>();

    private static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            nums.add(sc.nextInt());
        }

        List<Integer> res = mergeSort(nums);
        for (int x : res) {
            sb.append(x);
            sb.append('\n');
        }

        System.out.print(sb);
    }

    private static List<Integer> mergeSort(List<Integer> nums) {
        if (nums.size() < 2) {
            return nums;
        }
        int mid = nums.size() / 2;

        List<Integer> left = new ArrayList<>();
        List<Integer> right = new ArrayList<>();

        for (int i = 0; i < mid; i++) {
            left.add(nums.get(i));
        }

        left = mergeSort(left);

        for (int i = mid; i < nums.size(); i++) {
            right.add(nums.get(i));
        }

        right = mergeSort(right);

        return merge(left, right);
    }

    private static List<Integer> merge(List<Integer> left, List<Integer> right) {
        List<Integer> result = new ArrayList<>();

        int l = 0, r = 0;

        while (l < left.size() && r < right.size()) {
            if (left.get(l) <= right.get(r)) {
                result.add(left.get(l));
                l++;
            } else {
                result.add(right.get(r));
                r++;
            }
        }

        // 남은 요소들을 추가
        while (l < left.size()) {
            result.add(left.get(l));
            l++;
        }

        while (r < right.size()) {
            result.add(right.get(r));
            r++;
        }

        return result;
    }

}