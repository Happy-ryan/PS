import java.util.*;

public class Main {
    public static int n, k;
    public static int[] numbers;
    public static char[] alpabets;

    private static int mod = 0;


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        k = sc.nextInt();

        numbers = new int[k];
        alpabets = new char[k];

        for (int i = 0; i < k; i++) {
            int num = sc.nextInt();
            // Scanner - char 입력방법
            char al = sc.next().charAt(0);
            numbers[i] = num;
            alpabets[i] = al;            
        }
    
       char[] realWheel = new char[n];

       for (int i = 0; i < n; i++) {
            realWheel[i] = '?';
       }

        int finalCharIndex = 0;
        boolean 한칸_알파벳_중복 = false;
        for(int i = 0; i < k; i++) {
            mod = roate(numbers[i]);
            // System.out.print(fortuneWheel.getFirst() + ":" + alpabets[i]+"\n");
            // realWheel에 ?가 아니면서 이미 들어있던 문자와 다른 경우에는 알 수 없는 wheel이 된다.
            if (realWheel[mod] != '?' && realWheel[mod] != alpabets[i]) {
                한칸_알파벳_중복 = true;
            }
            realWheel[mod] = alpabets[i]; // 휠에 알파벳 할당
            finalCharIndex = mod;
        }

        if (isDuplicateAlpabet(realWheel) || 한칸_알파벳_중복) {
            System.out.println('!');
        }
        else {
            prettyPrint(realWheel, finalCharIndex);
        }
    }
    // mod는 default 0
    // 바퀴의 칸 수만큼 회전시키면 원상태로 회복
    public static int roate(int count) {
        mod += count;
        mod %= n;
        return mod;
    }

    public static void prettyPrint(char[] realWheel, int finalCharIndex) {
        int mod = finalCharIndex;
        StringBuilder br = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (mod == -1) {
                mod = n - 1;
            }
            br.append(realWheel[mod]);
            mod--;
        }
        System.out.println(br);
    }

    public static boolean isDuplicateAlpabet(char[] realWheel) {
        int[] used = new int[26];
        for (char ch: realWheel) {
            if (ch == '?') {
                continue;
            }
            used[(int)ch - 'A'] += 1;
            if (used[(int)ch - 'A'] > 1) {
                return true;
            }
        }
        return false;
    }
}