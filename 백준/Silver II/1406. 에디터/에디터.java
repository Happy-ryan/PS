import java.util.*;
import java.io.*;

class myArrayList<E> {
    /*    size: 실제 원소 개수
        elementData: 원소 보관함
        capacity: 원소 보관함 크기     */
    private static final int DEFAULT_CAPACITY = 10;
    private int size = 0;
    private Object[] elementData;

    public myArrayList() {
        elementData = new Object[DEFAULT_CAPACITY];
    }

    public myArrayList(int initialCapacity) {
        elementData = new Object[initialCapacity];
    }

    public void add(E e) {
        if (size == elementData.length) {
            growCapacity();
        }
        elementData[size++] = e;
    }

    private void growCapacity() {
        // 1.5배
        int newCapacity = elementData.length + (elementData.length >> 1);
        elementData = Arrays.copyOf(elementData, newCapacity);
    }

    public void insert(int idx, E e) {
        if (size == elementData.length) {
            growCapacity();
        }
/*       public static void arraycopy(Object src, int srcPos, Object dest, int destPos, int length)
        src: 원본 배열
        srcPos: 원본 배열에서 복사를 시작할 인덱스
        dest: 대상 배열
        destPos: 대상 배열에서 붙여넣기를 시작할 인덱스
        length: 복사할 요소의 수
        원본 배열의 일부 또는 전체 요소를 대상 배열의 지정된 위치에 복사
        */
        // 1 2 3 4 5 인덱스1에 10을 넣을 예정: size(5) - idx(1) = 4
        // 1 10 [2 3 4 5]
        int copyLength = size - idx;
        System.arraycopy(elementData, idx, elementData, idx + 1, copyLength);
        elementData[idx] = e;
        size++;
    }

    public void remove(int idx) {
        if (idx < 0 || idx >= size) {
            throw new IndexOutOfBoundsException("Out of IndexError");
        }
        // 1 2 [3 4 5] 에서 인덱스1인 원소 지울 예정: size(5) - idx(1) - 1(제거하는 원소는 1개) = 3
        // 1 [3 4 5] 3이 idx 1로 변경!
        int copyLength = elementData.length - idx - 1;
        System.arraycopy(elementData, idx + 1, elementData, idx, copyLength);
        size--;
    }

    public void finalElemnetRemove() {
        size--;
    }

    public E get(int idx) {
        if (idx < 0 || idx >= size) {
            throw new IndexOutOfBoundsException("Out of IndexError");
        }
        return (E) elementData[idx];
    }

    public int size() {
        return size;
    }

}

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();

        myArrayList<Character> leftArrayList = new myArrayList<>(10000000);
        myArrayList<Character> rightArrayList = new myArrayList<>(10000000);


        for (int i = 0; i < input.length(); i++) {
            leftArrayList.add(input.charAt(i));
        }

        int m = Integer.parseInt(br.readLine());
        for (int i = 0; i < m; i++) {
            char[] cmd = br.readLine().toCharArray();
            if (cmd[0] == 'P') {
                leftArrayList.add(cmd[2]);
            } else if (cmd[0] == 'D') {
                if (rightArrayList.size() == 0) {
                    continue;
                }
                char rightFinalElement = rightArrayList.get(rightArrayList.size() - 1);
                rightArrayList.finalElemnetRemove();
                leftArrayList.add(rightFinalElement);

            } else if (cmd[0] == 'L') {
                if (leftArrayList.size() == 0) {
                    continue;
                }
                char leftFinalElement = leftArrayList.get(leftArrayList.size() - 1);
                leftArrayList.finalElemnetRemove();
                rightArrayList.add(leftFinalElement);
            } else if (cmd[0] == 'B') {
                if (leftArrayList.size() == 0) {
                    continue;
                }
                leftArrayList.finalElemnetRemove();
            }
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        for (int i = 0; i < leftArrayList.size(); i++) {
            bw.write(leftArrayList.get(i));
        }
        for (int i = rightArrayList.size() - 1; i >= 0; i--){
            bw.write(rightArrayList.get(i));
        }
        bw.flush();
    }
}
