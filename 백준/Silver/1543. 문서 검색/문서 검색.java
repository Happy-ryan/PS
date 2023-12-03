import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String string1 = br.readLine();
        String string2 = br.readLine();

        // 기존 문자열 - string2 대체한 문자열 차이 = 대체된 문자열의 총 길이
        // 대체된 문자열의 총 길이 / 대체 문자열의 길이
        int k = string1.length() - string1.replaceAll(string2, "").length();

        System.out.println(k / string2.length());

    }
}
