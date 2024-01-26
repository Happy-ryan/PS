import java.util.*;

public class Main {
    public static int n, k;
    public static int[] numbers;
    public static char[] alpabets;

    public static Deque<Integer> fortuneWheel = new ArrayDeque<>();

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
    

        for (int i = 0; i < n; i++) {
            fortuneWheel.add(i);
        }

       char[] realWheel = new char[n];

       for (int i = 0; i < n; i++) {
            realWheel[i] = '?';
       }

        int finalCharIndex = 0;
        boolean 한칸_알파벳_중복 = false;
        for(int i = 0; i < k; i++) {
            roate(numbers[i]);
            // System.out.print(fortuneWheel.getFirst() + ":" + alpabets[i]+"\n");
            // realWheel에 ?가 아니면서 이미 들어있던 문자와 다른 경우에는 알 수 없는 wheel이 된다.
            if (realWheel[fortuneWheel.getFirst()] != '?' && realWheel[fortuneWheel.getFirst()] != alpabets[i]) {
                한칸_알파벳_중복 = true;
            }

            realWheel[fortuneWheel.getFirst()] = alpabets[i]; // 휠에 알파벳 할당
            finalCharIndex = fortuneWheel.getFirst();
        }

        if (isDuplicateAlpabet(realWheel) || 한칸_알파벳_중복) {
            System.out.println('!');
        }
        else {
            prettyPrint(realWheel, finalCharIndex);
        }

    }
    // 화살표는 인덱스0번만 가르킨다!
    // ABC - 원판 
    // 각 1번씩 회전의 상태 변화 관찰: ABC > CAB > BCA > ABC
    // 맨뒤가 맨앞으로 오도록!
    // 바퀴의 칸 수만큼 회전시키면 원상태로 회복
    public static void roate(int count) {
        count %= n;
        for (int t = 0; t < count; t++){
            int tmp = fortuneWheel.removeLast();
            fortuneWheel.addFirst(tmp);
        }
    }

    public static void prettyPrint(char[] realWheel, int finalCharIndex) {
        int mod = finalCharIndex;
        StringBuilder br = new StringBuilder();
        for (int i = 0; i < n; i++) {
            mod %= n;
            br.append(realWheel[mod]);
            mod++;
        }
        System.out.println(br.toString());
    }

    public static boolean isDuplicateAlpabet(char[] realWheel) {
        Set<Character> charSet = new HashSet<>();
        for (char ch: realWheel) {
            if (ch == '?') {
                continue;
            }
            if (charSet.contains(ch)) {
                return true;
            } else {
                charSet.add(ch);
            }
        }
        return false;
    }

}