import java.util.*;

class Pair implements Comparable<Pair> {
    int number, fre;

    public Pair(int number, int fre) {
        this.number = number;
        this.fre = fre;
    }

    // compareTo 메서드 오버라이드
    @Override
    public int compareTo(Pair other) {
        // fre를 기준으로 정렬
        // this.free = o1, other.free = o2를 의미함.
        // o1 - o2 : 오름차순
        // o2 - o1 : 내림차순
        return Integer.compare(other.fre, this.fre);
    }
}

public class Main {

    private static int n, c;
    private static Map<Integer, Integer> freqMap = new LinkedHashMap<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        c = sc.nextInt();

        for (int i = 0; i < n; i++) {
            int num = sc.nextInt();
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        List<Pair> arr = new ArrayList<>();
        for (int num : freqMap.keySet()) {
            arr.add(new Pair(num, freqMap.get(num)));
        }
        
        Collections.sort(arr);

        for (int i = 0; i < arr.size(); i++) {
            for (int j = 0; j < arr.get(i).fre; j++) {
                System.out.printf("%d ", arr.get(i).number);
            }
        }
    }
}