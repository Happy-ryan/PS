import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    private static int w, h, p, q, t;
    // 수평이동(오른쪽, 왼쪽)
    private static int[] dx = new int[]{1, -1};
    // 수직이동(위, 아래)
    private static int[] dy = new int[]{1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        String inputWH = br.readLine();
        st = new StringTokenizer(inputWH);

        w = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());

        String inputPQ = br.readLine();
        st = new StringTokenizer(inputPQ);

        p = Integer.parseInt(st.nextToken());
        q = Integer.parseInt(st.nextToken());

        String inputTime = br.readLine();
        st = new StringTokenizer(inputTime);
        t = Integer.parseInt(st.nextToken());
        // 초기 방향: 오른쪽 위(0, 0)
        horizontalSimulate(t, 0);
        verticalSimulate(t, 0);
    }

    private static void horizontalSimulate(int t, int d) {
        // 수평주기 w = 6일 때 초기값: x = 2 (d: ->)
        // 2 3 4 5 6 5 4 3 2(<-) 1 '2(->)': 2W
        t %= 2 * w;
        for (int i = 1; i <= t; i++) {
            d = horizontalMovement(p, d);
            p += dx[d];
        }
        System.out.printf("%d ", p);
    }

    private static void verticalSimulate(int t, int d) {
        t %= 2 * h;
        for (int i = 1; i <= t; i++) {
            d = verticalMovement(q, d);
            q += dy[d];
        }
        System.out.printf("%d", q);
    }

    private static int horizontalMovement(int p, int d) {
        if (p == w || p == 0) {
            return (d + 1) % 2;
        }
        return d;
    }

    private static int verticalMovement(int q, int d) {
        if (q == h || q == 0) {
            return (d + 1) % 2;
        }
        return d;
    }
}