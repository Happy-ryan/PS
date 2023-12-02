import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        // 기준: 0시 0분 0초 !
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] presentTime = br.readLine().split(":");
        String[] inputTime = br.readLine().split(":");

        int presentSecond = changeToSecond(presentTime);
        int inputSecond = changeToSecond(inputTime);

        inputSecond = (inputSecond <= presentSecond) ? inputSecond + (24 * 60 * 60) : inputSecond;

        System.out.println(changeHHMMSS(presentSecond, inputSecond));

    }

    private static int changeToSecond(String[] times) {
        int hour = Integer.parseInt(times[0]);
        int minute = Integer.parseInt(times[1]);
        int second = Integer.parseInt(times[2]);

        return hour * 3600 + minute * 60 + second;
    }

    private static String changeHHMMSS(int startTime, int inputTime) {
        int time = inputTime - startTime;
        int hour = time / 3600;
        int minute = (time - hour * 3600) / 60;
        int second = (time - hour * 3600 - minute * 60);
        return String.format("%02d:%02d:%02d", hour, minute, second);
    }
}
