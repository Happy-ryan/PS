import java.util.*;
// 틀린이유: 0 + 0
// 틀린이유2: -10 40 의 경우 -10이 길이가 더 길어서 40보다 크다고 인식한다.(10과 40이 비교되었을때)
// 2 4 6 8만 틀린이유: -100 100 도 시작이 0이 된다. 결과 프린트할 때도 removeFirstZeros사용해여함.
public class Main {


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String a = sc.next();
        String b = sc.next();

        // 배열에 집어넣으면 '0' ~ '9'만 존재함!!
        // '0' ~ '9'는 아스키코드 상 연속적 배치이므로 실제 덧셈/빨셈과 같은 값이 나올 것
        // '9' - '1' = 8
        char[] A = new char[a.length()];
        for (int i = 0; i < a.length(); i++) {
            A[i] = a.charAt(i);
        }

        char[] B = new char[b.length()];
        for (int i = 0; i < b.length(); i++) {
            B[i] = b.charAt(i);
        }
        
        choose(A, B);
        
    
    }
    private static void choose(char[] A, char[] B) {
        if (A[0] == '-' && B[0] == '-') {
            // 더한 다음 - 만 붙이면 된다.
            // -는 '0'으로 제거해주자.
            System.out.print('-');
            A[0] = '0';
            B[0] = '0';
            add(A, B);
        }
        else if (A[0] != '-' && B[0] != '-') {
            add(A, B);
        }
        else if (A[0] == '-' && B[0] != '-') {
            A[0] = '0';
            char[] newA = removeFirstZeros(A);
            // A가 더 크니까 반드시 -가 붙어야함.
            if (isABiggeThanB(newA, B)) {
                System.out.print('-');
                subtract(newA, B);
            }
            else {
                subtract(B, newA);
            }
        }
        else if (A[0] != '-' && B[0] == '-') {
            B[0] = '0';
            char[] newB = removeFirstZeros(B);
            if (isABiggeThanB(A, newB)) {
                subtract(A, newB);
            }
            // else가 잘못된 이유 > B >= A .. A = B 일 때 -0이 나오게 되는 문제가 발생함!!
            else {
                if(Arrays.equals(A, newB)) {
                    subtract(newB, A);
                }
                else {
                    System.out.print('-');
                    subtract(newB, A);
                }
            }
        }
    }
    // 덧셈 주의: 올림만 주의하면 된다!
    private static void add(char[] A, char[] B) {
        // 배열 - length / 문자열 - length()
        int n = Math.max(A.length, B.length);
        // 0 ~ n(인덱스 허용 범위)
        char[] result = new char[n +1];
        // tmp를 가지고 올림을 유지
        // 뒤에서부터 연산해야 올림 반영 가능.
        int tmp = 0;
        for (int i = 0; i <= n; i++) {
            int sum = tmp;
            if (A.length - 1 - i >= 0) {
                sum += A[A.length - 1 - i] - '0';
            }
            if (B.length - 1 - i >= 0) {
                sum += B[B.length - 1 - i] - '0';
            }
            // '0' (48) + sum(5) = '5' (53)
            // i = 0 > result[n] 가장 마지막 인덱스
            result[n - i] = (char) ((sum) % 10 + '0');
            tmp = sum / 10; 
        }

        char[] newResult = removeFirstZeros(result);
        System.out.print(newResult);
    
    }
    // 뺄셈- 내림 주의
    private static void subtract(char[] A, char[] B) {
        // A가 무조건 큰게 와야함!! 그리고 반드시 양수임!
        int n = A.length;
        char[] result = new char[n];
        int tmp = 0;
        for (int i = 0; i < n; i++) {
            int diff = tmp;
            if (A.length - 1 - i >= 0) {
                diff += A[A.length - 1 - i] - '0';
            }
            if (B.length - 1 - i >= 0) {
                diff -= B[B.length - 1 - i] - '0';
            }
            if (diff < 0) {
                diff += 10;
                // 내림
                tmp = -1;
            }
            else {
                tmp = 0;
            }
            result[n - 1 - i] = (char) (diff + '0');
        }

        char[] newResult = removeFirstZeros(result);
        System.out.print(newResult);
    }

    private static boolean isABiggeThanB(char[] A, char[] B) {
        // 길이가 더 길면 큰 수
        if (A.length != B.length) {
            return A.length > B.length; 
        }

        // 길이가 같은 경우, 각 자리수를 비교하여 큰 수를 가리키는 배열을 찾음
        for (int i = 0; i < A.length; i++) {
            if (A[i] != B[i]) {
                return A[i] > B[i];
            }
        }
        // 여기까지 왔다면 A와 B는 같은 수
        return false;
        }

    private static char[] removeFirstZeros(char[] A) {
        // 다른 숫자가 나오기 전까지 '0'이 어디까지 이어지는지 확인
        int startIndex = 0;
        while (startIndex < A.length && A[startIndex] == '0') {
            startIndex++;
        }

        if (startIndex == A.length) {
            return new char[] {'0'};
        }

        int resultSize = A.length - startIndex;
        char[] result = new char[resultSize];

        for (int i = startIndex; i < A.length; i++) {
            result[i - startIndex] = A[i];
        }

        return result;
    }
}