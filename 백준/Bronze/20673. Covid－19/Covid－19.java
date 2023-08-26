import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // p 2주동안 하나시 인구 100만명 당 일일 평균 신규 사례 수
        // q 2주동안 하나시 인구 100만명 당 일일 평균 신규 입원 건수
        int p, q;

        p = sc.nextInt();
        q = sc.nextInt();

        if(q > 30){
                System.out.print("Red");
        }
        else if(p <= 50 && q <= 10){
                System.out.print("White");   
        }
        else{
                System.out.print("Yellow");
        }
    }
}