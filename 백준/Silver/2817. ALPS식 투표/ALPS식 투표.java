import java.util.*;

class Pair implements Comparable<Pair> {
    char name;
    double score;
    public Pair(char name, double score) {
        this.name = name;
        this.score = score;
    }

    @Override
    public int compareTo(Pair other) {
        // score 기준 - 내림차순
        // o1(this), o2(other)
        return Double.compare(other.score, this.score);
    }
}

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int x = sc.nextInt();
        int n = sc.nextInt();

        List<Pair> scoreList = new ArrayList<>();
        // 14위 안에 못들어도 5퍼센트 이상의 경우 출력해야함!
        List<Character> overFivePercentPeople = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            // char받을 때 charAt 까먹지말기!
            char name = sc.next().charAt(0);
            int score = sc.nextInt();
            // 5퍼센트 미만은 고려 안함.
            if (score * 100 < x * 5) {
                continue;
            }
            overFivePercentPeople.add(name);
            for (int j = 1; j <= 14; j++) {
                scoreList.add(new Pair(name, (double)(score) / j)); // 소수점까지 나오도록!
            }
        }
        // 상위 14개를 얻기 위해서 점수로 정렬
        Collections.sort(scoreList);
        // 5퍼센트 이상든 사람의 목록 - 사전순 출력
        Collections.sort(overFivePercentPeople);

        int[] voteCount = new int[26];
        for (int i = 0; i < 14; i++) {
            voteCount[(int) scoreList.get(i).name - 'A']++;
        }

        for (char name : overFivePercentPeople) {
            System.out.printf("%s %d\n", name, voteCount[(int)(name - 'A')]);

        }

    }
}