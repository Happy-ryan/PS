import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        String[] dir = {"E", "S", "W", "N"};
        int cur_dir = 3;

        Scanner sc = new Scanner(System.in);

        for (int i = 0; i < 10; i++) {
            int command = sc.nextInt();
            // 1 시계방향 / 2 180도 / 3 반시계방향
            // 동(0)남(1)서(2)북(3)
            if (command == 1) {
                cur_dir = (cur_dir + 1) % 4;
            } else if (command == 2) {
                cur_dir = (cur_dir + 2) % 4;
            } else if (command == 3) {
                cur_dir = (cur_dir - 1 + 4) % 4;
            }
        }

        System.out.println(dir[cur_dir]);
    }
}