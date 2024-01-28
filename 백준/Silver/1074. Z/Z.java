import java.util.*;


public class Main {

    private static int cnt = 0;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int r = sc.nextInt();
        int c = sc.nextInt();
        find((int) Math.pow(2, n), r, c);
        System.out.println(cnt);
    }   

    private static void find(int w, int r, int c) {
        if (w == 2) {
            if (r % 2 == 0 && c % 2 == 0) {
                cnt += 0;
            }
            else if (r % 2 == 0 && c % 2 == 1) {
                cnt += 1;
            }
            else if (r % 2 == 1 && c % 2 == 0) {
                cnt += 2;
            }
            else if (r % 2 == 1 && c % 2 == 1) {
                cnt += 3;
            }
            return;
        }
        if (0 <= r  && r < w /2 && 0 <= c && c < w / 2) {
            find(w / 2, r, c);
            cnt += w * w / 4 * 0;
        }
        else if (0 <= r && r < w /2 && w / 2 <= c && c < w) {
            find(w / 2, r, c - w / 2);
            cnt += w * w / 4 * 1;
        }
        else if (w /2 <= r && r < w && 0 <= c && c < w / 2) {
            find(w / 2, r - w / 2, c);
            cnt += w * w / 4 * 2;
        }
        else if (w / 2 <=  r && r < w && w / 2 <= c && c < w) {
            find(w / 2, r - w / 2, c - w / 2);
            cnt += w * w / 4 * 3;
        }
    }
}