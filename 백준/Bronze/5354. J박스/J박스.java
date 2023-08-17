import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n;

        n = sc.nextInt();
        for(int i = 0; i < n ; i++){
            int x = sc.nextInt();
            for(int j=0; j < x; j++){
                if(j == 0 || j == (x - 1)){
                    for(int z = 0; z < x; z++){
                        System.out.print('#');
                    }
                }
                else{
                    for(int z = 0; z < x; z ++){
                        if (z == 0 || z == (x - 1)){
                            System.out.print('#');
                        }
                        else{
                            System.out.print('J');
                        }
                    }
                }
                System.out.println("");
            }
            System.out.println("");
        }
    }
}