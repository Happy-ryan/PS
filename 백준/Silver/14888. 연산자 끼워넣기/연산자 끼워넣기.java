import java.util.*;

public class Main {
    private static int n;
    private static int[] numbers, cmds;

    private static List<Integer> ans = new ArrayList<>();

    private static int maxVal = -1000000000;
    private static int minVal = 1000000000;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        numbers = new int[n];
        for (int i = 0; i < n; i++) {
            numbers[i] = sc.nextInt();
        }
        cmds = new int[4];
        for (int i = 0; i < 4; i++) {
            cmds[i] = sc.nextInt();
        }

        back(0);

        System.out.printf("%d\n%d", maxVal, minVal);
    }
    // 중간에 계산되는 결과도 -10억 ~ 10억보다 작음 > int로 해도 무관함.
    // 숫자와 연산자를 한 번에 같이 볼 필요가 없음!
    private static void back(int level) {
        // 연산자의 수는 숫자 n개보다 1개 적음.
        if (level == n - 1) {
                int res = cal(numbers, ans);
                maxVal = Math.max(maxVal, res);
                minVal = Math.min(minVal, res);
            return;
        }

        for(int i = 0; i < 4; i++) {
            if (cmds[i] != 0) {
                ans.add(i);
                cmds[i] -= 1;
                back(level + 1);
                cmds[i] += 1;
                ans.remove(ans.size() - 1);
            }
        }
    }
    // 계산하기, 숫자배열 & 연산자 배열
    private static int cal(int[] numbers, List<Integer> cmds) {
        int ans = numbers[0];
        for (int i = 1; i < n; i++) {
            if (cmds.get(i - 1) == 0) {
                ans += numbers[i];
            }
            else if (cmds.get(i - 1) == 1) {
                ans -= numbers[i];
            }
            else if (cmds.get(i - 1) == 2) {
                ans *= numbers[i];
            }
            else {
                if (ans > 0) {
                    ans /= numbers[i];
                }
                else {
                    int reverserAns = -ans;
                    reverserAns /= numbers[i];
                    ans = -reverserAns;
                }
            }
        }
        return ans;
    }
}