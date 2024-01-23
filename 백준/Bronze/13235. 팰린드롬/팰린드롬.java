import java.io.*;
import java.util.*;

public class Main {
    private static String string;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        string = br.readLine();
        if(palindrom(string)){
            System.out.println("true");
        }
        else{
            System.out.println("false");
        }

    } 

    private static boolean palindrom(String string){
        boolean res = true;
        for(int idx= 0; idx<string.length()/2; idx++){
            if(string.charAt(idx) == string.charAt(string.length()-idx-1)){
                continue;
            }else{
                res = false;
            }
        }
        return res;
    }
}